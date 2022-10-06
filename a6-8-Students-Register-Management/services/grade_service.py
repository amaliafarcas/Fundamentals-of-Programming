from src.domain.grade import Grade
from src.domain.grade_validator import GradeVal
from random import randint
import unittest
from src.repository.repository_exception import Exception
from src.services.undo_service import FunctionCall, Operation, CascadedOperation
from src.services.gnome_sort import gnomeSort, filter


class GradeSer:
    def __init__(self, grade_repo, student_service, discipline_service, undo_service):
        self.__repo = grade_repo
        self._validator = GradeVal()
        self.__studService = student_service
        self.__disService = discipline_service
        self.__undo_service = undo_service

    def add_grade_undo(self, stud_id, dis_id, gr):
        """
        adds a grade (undo/redo function)
        :param stud_id: student id
        :param dis_id: discipline id
        :param gr: grade
        :return:
        """
        grade = Grade(stud_id, dis_id, gr)
        self.__repo.add_gr(grade)

    def add_gr(self, gr):
        self.__repo.add_gr(gr)

    def add_grade(self, gr):
        """
        adds a grade
        :param gr: grade
        :return:
        """

        try:
            idd = gr.dis_id
            self.__disService.is_discipline(idd)
            ids = gr.stud_id
            self.__studService.is_student(ids)
            self._validator.validate(gr)
            delete_list = list()
            delete_list.append(gr)

            self.__repo.add_gr(gr)
            fc_undo = FunctionCall(self.__repo.delete_mult_grades, delete_list)
            fc_redo = FunctionCall(self.__repo.add_mult_grades, delete_list)
            cope = CascadedOperation()
            cope.add(Operation(fc_undo, fc_redo))
            self.__undo_service.record_operation(cope)

        except Exception as ve:
            raise ve
        return gr

    def delete_grade_undo(self, sid, did, gr):
        """
        deletes a grade (undo/redo function)
        :param sid: student id
        :param did: discipline id
        :param gr: grade
        :return:
        """
        grade = Grade(sid, did, gr)
        self.__repo.delete_gr(grade)

    def delete_gr(self, gr):
        """
        deletes a grade
        :param gr:
        :return:
        """
        self.__repo.delete_gr(gr)

    def delete_grade(self, stud_id, dis_id, gr):
        """
        deletes a grade
        :param stud_id: student id
        :param dis_id: discipline id
        :param gr: the grade that the given student has at the given discipline
        :return:
        """
        grade_list = self.__repo.show_grade()
        k = 0
        i = 0
        s = 0
        delete_list = list()
        while i < len(grade_list):
            if int(grade_list[i].stud_id) == int(stud_id) and int(grade_list[i].dis_id) == int(dis_id) \
                    and int(grade_list[i].grade) == int(gr):
                s = grade_list[i]
                delete_list.append(s)
                k = 1
            i += 1
        if k == 0:
            raise Exception("No grade to be removed")
        else:
            try:
                self.__repo.delete_gr(s)
                fc_undo = FunctionCall(self.__repo.add_mult_grades, delete_list)
                fc_redo = FunctionCall(self.__repo.delete_mult_grades, delete_list)
                cope = CascadedOperation()
                cope.add(Operation(fc_undo, fc_redo))
                self.__undo_service.record_operation(cope)

            except Exception as ve:
                raise ve
        return s

    def delete_studgrade(self, stud_id):
        """
        used for deleting the grades of a student that was removed from the repository
        :param stud_id: the student that was removed
        :return:
        """
        deleted_list = list()
        grade_list = self.__repo.show_grade()
        i = 0
        l = 0
        while i < len(grade_list):
            if int(grade_list[i].stud_id) == int(stud_id):
                s = grade_list[i]
                deleted_list.append(s)
                l = 1
            i += 1
        if l > 0:
            try:
                self.__repo.delete_mult_grades(deleted_list)
                fc_undo = FunctionCall(self.__repo.add_mult_grades, deleted_list)
                fc_redo = FunctionCall(self.__repo.delete_mult_grades, deleted_list)
                cope = CascadedOperation()
                cope.add(Operation(fc_undo, fc_redo))

                fname = self.__studService.search_fn_stud_id(stud_id)
                sname = self.__studService.search_sn_stud_id(stud_id)
                fc_undo = FunctionCall(self.__studService.add_student_undo, stud_id, fname, sname)
                fc_redo = FunctionCall(self.__studService.delete_student_id, stud_id)
                cope.add(Operation(fc_undo, fc_redo))

                self.__undo_service.record_operation(cope)
            except Exception as ve:
                raise ve


    def delete_disgrade(self, dis_id):
        """
        used for deleting the graded of all students for a discipline that was removed from the repository
        :param dis_id: the discipline that was removed
        :return:
        """
        deleted_list = list()
        grade_list = self.__repo.show_grade()
        l = 0
        i = 0
        while i < len(grade_list):
            if int(grade_list[i].dis_id) == int(dis_id):
                s = grade_list[i]
                deleted_list.append(s)
                l = 1
            i += 1
        if l > 0:
            try:
                self.__repo.delete_mult_grades(deleted_list)
                fc_undo = FunctionCall(self.__repo.add_mult_grades, deleted_list)
                fc_redo = FunctionCall(self.__repo.delete_mult_grades, deleted_list)
                cope = CascadedOperation()
                cope.add(Operation(fc_undo, fc_redo))

                name = self.__disService.search_n_dis_id(dis_id)
                fc_undo = FunctionCall(self.__disService.add_dis_undo, dis_id, name)
                fc_redo = FunctionCall(self.__disService.delete_discipline_id, dis_id)
                cope.add(Operation(fc_undo, fc_redo))

                self.__undo_service.record_operation(cope)
            except Exception as ve:
                raise ve

    def modify_grade(self, stud_id, dis_id, o, n):
        """
        modifies a grade (undo/redo function)
        :param stud_id: student id
        :param dis_id: discipline id
        :param o: old grade
        :param n: new grade
        :return:
        """
        self.__repo.mod_grade(stud_id, dis_id, o, n)

    def mod_grade(self, stud_id, dis_id, o, n):
        """
        modifies a grade
        :param stud_id: student id
        :param dis_id: discipline id
        :param o: old grade
        :param n: new grade
        :return:
        """
        grade_list = self.__repo.show_grade()
        k = 0
        i = 0
        while i < len(grade_list):
            if int(grade_list[i].stud_id) == int(stud_id) and int(grade_list[i].dis_id) == int(dis_id) \
                    and int(grade_list[i].grade) == int(o):

                k = 1
            i += 1
        if k == 0:
            raise Exception("No grade to be modified")
        else:
            try:
                self.__repo.mod_grade(stud_id, dis_id, o, n)
                fc_undo = FunctionCall(self.modify_grade, stud_id, dis_id, n, o)
                fc_redo = FunctionCall(self.modify_grade, stud_id, dis_id, o, n)
                cope = CascadedOperation()
                cope.add(Operation(fc_undo, fc_redo))
                self.__undo_service.record_operation(cope)

            except Exception as ve:
                raise ve

    def generate_grades(self):
        """
        generates grades for each student at each discipline
        :return:
        """
        stud_list, length_stud = self.__studService.show_stud_len()
        dis_list, length_dis = self.__disService.show_dis_len()
        i = 0

        while i < length_stud:
            j = 0
            si = stud_list[i].id
            while j < length_dis:

                di = dis_list[j].id
                gr = randint(1, 10)
                grade = Grade(si, di, gr)
                self.__repo.add_gr(grade)
                j += 1
            i += 1

    def show_grade(self):
        """

        :return: the list of grades
        """
        return self.__repo.show_grade()

    def sort_gr(self):
        grade_list = self.__repo.show_grade()
        sorted_list = list()
        k = 0
        for s in grade_list:
            k = 1
            sorted_list.append([s.stud_id, s.dis_id, s.grade])
        if k == 0:
            raise Exception("Grade list is empty")
        else:
            sorted_list = gnomeSort(sorted_list, len(sorted_list), 1)
            return gnomeSort(sorted_list, len(sorted_list), 0)

    def average_grades_stud(self):
        student_list, length_s = self.__studService.show_stud_len()
        discipline_list, length_d = self.__disService.show_dis_len()
        gr_list = self.sort_gr()
        failing_list = list()
        i = 0
        while i < length_s:
            sid = student_list[i].id
            j = 0
            while j < length_d:
                did = discipline_list[j].id
                su = int(0)
                k = int(0)
                l = 0
                while l < len(gr_list):
                    if int(gr_list[l][0]) == int(sid) and int(gr_list[l][1]) == int(did):
                        su += int(gr_list[l][2])
                        k += 1
                    l += 1
                if k != 0:
                    av = su / k
                    failing_list.append([student_list[i].id, student_list[i].fname, student_list[i].sname,
                                             discipline_list[j].id, discipline_list[j].name, av])
                j += 1
            i += 1
        return failing_list

    def students_failing(self):
        s = []
        tempArray = []
        tempArray = filter(tempArray, self.average_grades_stud())
        for i in range(0, len(tempArray)):
            if tempArray[i][5] < 5:
                s.append([tempArray[i][0], tempArray[i][1], tempArray[i][2], tempArray[i][3], tempArray[i][4]])  # we put in the list the student
        return s

    def average_students(self):
        student_list, length_s = self.__studService.show_stud_len()
        discipline_list, length_d = self.__disService.show_dis_len()
        grade_list = self.sort_gr()
        best_list = list()
        i = 0
        while i < length_s:
            sid = student_list[i].id
            su = int(0)
            k = int(0)
            j = 0
            while j < length_d:
                did = discipline_list[j].id
                l = 0
                while l < len(grade_list):

                    if int(grade_list[l][0]) == int(sid) and int(grade_list[l][1]) == int(did):
                        su += int(grade_list[l][2])
                        k += 1
                    l += 1
                j += 1
            if k != 0:
                av = su / k
                best_list.append([student_list[i].id, student_list[i].fname, student_list[i].sname, av])
            i += 1
        return best_list

    def best_students(self):
        s = []
        tempArray = []
        tempArray = filter(tempArray, self.average_students())
        for i in range(0, len(tempArray)):
            if tempArray[i][3] > 5:
                s.append([tempArray[i][0], tempArray[i][1], tempArray[i][2], tempArray[i][3]])  # we put in the list the student
        return gnomeSort(s, len(s), 3)

    def dis_average(self):
        discipline_list, length_d = self.__disService.show_dis_len()
        grade_list = self.__repo.show_grade()
        dis_average = list()
        i = 0
        while i < length_d:
            did = discipline_list[i].id
            su = 0
            k = 0
            l = 0
            while l < len(grade_list):
                if int(grade_list[l].dis_id) == int(did):
                    su += int(grade_list[l].grade)
                    k += 1
                l += 1
            if k != 0:
                av = su / k
                dis_average.append([discipline_list[i].id, discipline_list[i].name, av])
            i += 1
        return dis_average

    def discipline_average(self):
        s = []
        tempArray = []
        tempArray = filter(tempArray, self.dis_average())
        for i in range(0, len(tempArray)):
             s.append([tempArray[i][0], tempArray[i][1], tempArray[i][2]])  # we put in the list the student
        return gnomeSort(s, len(s), 22)


class GradeServTest(unittest.TestCase):
    def setup(self, grade_repo, student_service, discipline_service, undo_service):
        """
        Runs before any of the tests
        Used to set up the class so that tests can be run

        :return: None
        """
        self._grepo = grade_repo
        self._srepo = student_service
        self._drepo = discipline_service
        self._ser = GradeSer(grade_repo, student_service, discipline_service, undo_service)
        self._grade = Grade(258, 1978, 5)
        self._repo.add_grade(self._grade)

    def test_repo_elem(self):
        # test add
        self.assertEqual(len(self._repo), 21)
        self._ser.add_grade(Grade(425, 2589, 8))
        self._ser.add_grade(Grade(559, 2597, 2))
        self.assertEqual(len(self._repo), 23)

        # test delete
        last_grade = self._repo[len(self._repo)-1]
        stud_id_lg = last_grade.stud_id
        dis_id_lg = last_grade.dis_id
        grade_last_grade = last_grade.grade
        self._ser.delete_grade(stud_id_lg, dis_id_lg, grade_last_grade)
        self.assertEqual(len(self._repo), 7)

        # test update
        last_grade = self._repo[len(self._repo)-1]
        stud_id_lg = last_grade.stud_id
        dis_id_lg = last_grade.dis_id
        grade_last_grade = last_grade.grade
        self._repo.mod_grade(stud_id_lg, dis_id_lg, grade_last_grade, 9)
        last_grade = self._repo[len(self._repo) - 1]
        grade_last_grade = last_grade.grade
        self.assertEqual(grade_last_grade, 9)

    def tearDown(self) -> None:
        """
        Runs after all the tests have completed
        Used to close the test environment (clase files, DB connections, deallocate memory)

        :return: None
        """
        self._repo = None


def filter(tempArray,currentArray):
    for e in currentArray:
        tempArray.append(e)
    return tempArray
