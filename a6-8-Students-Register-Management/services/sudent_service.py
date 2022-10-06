from src.domain.student import Student
from src.domain.student_validator import StudVal
from random import randint, choice
import unittest
from src.repository.repository_exception import Exception
from src.services.undo_service import FunctionCall, CascadedOperation, Operation
from src.services.gnome_sort import gnomeSort


class StudentService:
    def __init__(self, student_repo, undo_service):
        self.__repo = student_repo
        self.__undo_service = undo_service
        self._validator = StudVal()
        self.fname_list = ['Pop', 'Crisan', 'Padurar', 'David', 'Andrei',
                           'Man', 'Negrean', 'Muresan', 'Moldovan', 'Cozorici']
        self.sname_list = ['Vlad', 'Corina', 'Ciprian', 'Alexandra', 'Tudor',
                           'Alexandra', 'Ana', 'Dan', 'Laurentiu', 'Raluca', 'Stefan', 'Bogdan', 'David']

    def add_student_undo(self, sid, fname, sname):
        """
        adds a student (undo/redo function)
        :param sid: id
        :param fname: first name
        :param sname: second name
        :return:
        """
        stud = Student(sid, fname, sname)
        self.__repo.add_student(stud)

    def add_student(self, stud):
        """
        adds a student
        :param stud: the student
        :return:
        """
        self.__repo.add_student(stud)

    def add_stud(self, stud):
        """
        adds a new student
        :param stud: the student that needs to be added
        :return:
        """

        try:
            self._validator.validate(stud)
            self.__repo.add_student(stud)
            fc_undo = FunctionCall(self.delete_stud, stud.id)
            fc_redo = FunctionCall(self.add_student_undo, stud.id, stud.fname, stud.sname)
            cope = CascadedOperation()
            cope.add(Operation(fc_undo, fc_redo))
            self.__undo_service.record_operation(cope)

        except Exception as ve:
            raise ve
        return stud

    def delete_student(self, stud_id, fname, sname):
        """
        deletes a student (undo/redo function)
        :param stud_id: id
        :param fname: first name
        :param sname: second name
        :return:
        """
        s = Student(stud_id, fname, sname)
        self.__repo.delete_stud(s)

    def delete_student_id(self, stud_id):
        """
        deletes a student by id
        :param stud_id:
        :return:
        """
        self.__repo.delete_stud_id(stud_id)

    def delete_stud(self, stud_id):
        """
        deletes a student with a given id
        :param stud_id: the id of the student
        :return:
        """
        stud_list = self.__repo.show_stud()
        self._validator.validate_id(stud_id)
        k = -1
        i = 0
        s = 0
        while i < len(stud_list):

            if int(stud_list[i].id) == int(stud_id):
                s = stud_list[i]
                k = i

            i += 1
        if k == -1:
            raise Exception("No student to be removed")
        else:
            try:
                self.__repo.delete_stud(s)
                """
                fc_undo = FunctionCall(self.add_student_undo, s.id, s.fname, s.sname)
                fc_redo = FunctionCall(self.delete_student,  s.id, s.fname, s.sname)
                cope = CascadedOperation()
                cope.add(Operation(fc_undo, fc_redo))
                self.save_cope(Operation(fc_undo, fc_redo))
                """
            except Exception as ve:
                raise ve
        return s

    def modify_stud(self, stud_id, nf, ns):
        """
        modifies a student (undo/redo function)
        :param stud_id: id
        :param nf: new first name
        :param ns: new second name
        :return:
        """
        self.__repo.mod_stud(stud_id, nf, ns)

    def mod_stud(self, stud_id, nf, ns):
        """
        modifies a student
        :param stud_id: id
        :param nf: new first name
        :param ns: new second name
        :return:
        """
        stud_list = self.__repo.show_stud()
        k = 0
        i = 0
        onf = 0
        ons = 0
        while i < len(stud_list):
            if int(stud_list[i].id) == int(stud_id):
                k = 1
                onf = stud_list[i].fname
                ons = stud_list[i].sname
            i += 1
        if k == 0:
            raise Exception("No student to be modified")
        else:
            try:
                self.__repo.mod_stud(stud_id, nf, ns)
                fc_undo = FunctionCall(self.modify_stud, stud_id, onf, ons)
                fc_redo = FunctionCall(self.modify_stud, stud_id, nf, ns)
                cope = CascadedOperation()
                cope.add(Operation(fc_undo, fc_redo))
                self.__undo_service.record_operation(cope)

            except Exception as ve:
                raise ve

    def generate_students(self, n):
        """
        generates a list of n(=5) students
        :param n: ne number of students ot be generated
        :return:
        """
        k = 1970
        for i in range(n):
            d = k
            f = choice(self.fname_list)
            s = choice(self.sname_list)
            stud = Student(d, f, s)
            self.__repo.add_student(stud)
            e = randint(1, 4)
            k = k + e

    def show_stud(self):
        """

        :return: the list of students
        """
        return self.__repo.show_stud

    def show_stud_len(self):
        """

        :return: the list of students
        """
        listt = list()
        listt, le = self.__repo.show_stud_len()
        return listt, le

    def sort_stud(self):
        stud_list = self.__repo.show_stud()
        s_list = list()
        k = 0
        for s in stud_list:
            s_list.append([s.id, s.fname, s.sname])
            k = 1
        if k == 0:
            raise Exception("Student list is empty")
        else:
            return gnomeSort(s_list, len(s_list), 0)


    def is_student_rem(self, sid):
        """
        verifies if a student with a given id is in the list of students
        :param sid: the id the has to me verified
        :return:
        """
        st = self.__repo.show_stud()
        k = 0
        for s in st:
            if int(s.id) == int(sid):
                k = 1
        if k == 0:
            raise Exception("No student to be removed")
        else:
            return True

    def is_student(self, sid):
        """
        verifies if a student with a given id is in the list of students
        :param sid: the id the has to me verified
        :return:
        """
        st = self.__repo.show_stud()
        k = 0
        for s in st:
            if int(s.id) == int(sid):
                k = 1
        if k == 0:
            raise Exception("No student with such id")
        else:
            return True

    def is_student_true(self, sid):
        """
        verifies if a student with a given id is in the list of students
        :param sid: the id the has to me verified
        :return:
        """
        st = self.__repo.show_stud()
        k = 0
        for s in st:
            if int(s.id) == int(sid):
                k = 1
        if k == 0:
            return False
        else:
            return True

    def search_id_conditions(self, sid):
        stud_list = self.__repo.show_stud()
        k = 0
        s_list = list()
        for s in stud_list:
            if int(s.id) == int(sid) or sid in str(s.id):
                k = 1
                s_list.append([s.id, s.fname, s.sname])
        if k == 0:
            raise Exception("No student with such id")
        else:
            return s_list

    def search_stud_id(self, sid):
        """
        search for a student with a given id/partial id
        :param sid: the id/partial id
        :return: a list of the matching ids (and the names of the students)

        stud_list = self.__repo.show_stud()
        k = 0
        s_list = list()
        for s in stud_list:
            if int(s.id) == int(sid) or sid in str(s.id):
                k = 1
                s_list.append([s.id, s.fname, s.sname])
        if k == 0:
            raise Exception("No student with such id")
        else:
            return s_list
        """
        s = []
        tempArray = []
        tempArray = filter(tempArray, self.search_id_conditions(sid))
        for i in range(0, len(tempArray)):
            s.append([tempArray[i][0], tempArray[i][1], tempArray[i][2]])  # we put in the list the student
        return s

    def search_s_id(self, sid):
        """
        search for a student with a given id/partial id
        :param sid: the id/partial id
        :return: a list of the matching ids (and the names of the students)
        """
        stud_list = self.__repo.show_stud()
        k = 0
        stud = 0
        for s in stud_list:
            if int(s.id) == int(sid):
                k = 1
                stud = s
        if k == 0:
            raise Exception("No student with such id")
        else:
            return stud

    def search_fn_stud_id(self, sid):
        """
        search for a student with a given id/partial id
        :param sid: the id/partial id
        :return: a list of the matching ids (and the names of the students)
        """
        stud_list = self.__repo.show_stud()
        k = 0
        fn = 0
        for s in stud_list:
            if int(s.id) == int(sid):
                k = 1
                fn = s.fname
        if k == 0:
            raise Exception("No student with such id")
        else:
            return fn

    def search_sn_stud_id(self, sid):
        """
        search for a student with a given id/partial id
        :param sid: the id/partial id
        :return: a list of the matching ids (and the names of the students)
        """
        stud_list = self.__repo.show_stud()
        k = 0
        sn = 0
        for s in stud_list:
            if int(s.id) == int(sid):
                k = 1
                sn = s.sname
        if k == 0:
            raise Exception("No student with such id")
        else:
            return sn

    def search_stud_pname(self, name):
        """
        search for students with a given name/partial name
        !The user introduces only ONE name/partial name (first name or second name)
        :param name: the name/partial name
        :return: a list of matching names (with the id of the students)
        """
        stud_list = self.__repo.show_stud()
        k = 0
        s_list = list()
        for s in stud_list:
            f = s.fname
            sn = s.sname
            if name.lower() in str(f).lower() or name.lower() in str(sn).lower():
                s_list.append([s.id, s.fname, s.sname])
                k = 1
        if k == 0:
            raise Exception("No student with such name")
        else:
            return s_list

    def search_stud_ename(self, fname, sname):
        """
        search for students with a given name/partial name
        !The user introduces BOTH names/partial names (first name and second name)
        :param fname: the first name/partial name
        :param sname: the second name/partial name
        :return: a list of matching names (with the id of the students)
        """
        stud_list = self.__repo.show_stud()
        k = 0
        s_list = list()
        for s in stud_list:
            f = s.fname
            sn = s.sname
            if fname.lower() in str(f).lower() and sname.lower() in str(sn).lower():
                s_list.append([s.id, s.fname, s.sname])
                k = 1
        if k == 0:
            raise Exception("No student with such name")
        else:
            return s_list


class StudentRepoTest(unittest.TestCase):
    def setup(self, student_repo, undo_service):
        """
        Runs before any of the tests
        Used to set up the class so that tests can be run

        :return: None
        """
        self._repo = student_repo
        self._ser = StudentService(self._repo, undo_service)
        self._student = Student(1007, 'Sara', 'Bogdan')
        self._ser.add_stud(self._student)

    def test_repo_elem(self):
        # test add
        self.assertEqual(len(self._repo), 6)
        self._ser.add_stud(Student(3025, 'Mara', 'Morar'))
        self._ser.add_stud(Student(3559, 'Edi', 'Hadade'))
        self.assertEqual(len(self._repo), 8)

        # test delete
        last_student = self._repo[len(self._repo)-1]
        id_last_student = last_student.id
        self._repo.delete_stud(id_last_student)
        self.assertEqual(len(self._repo), 7)

        # test update
        last_student = self._repo[len(self._repo)-1]
        id_last_student = last_student.id
        self._repo.mod_stud(id_last_student, "lala", "ama")
        last_student = self._repo[len(self._repo) - 1]
        fname_last_stud = last_student.fname
        sname_last_stud = last_student.sname
        self.assertEqual(fname_last_stud, "lala")
        self.assertEqual(sname_last_stud, "ama")

        # test search stud id
        s_list = list()
        last_student = self._repo[len(self._repo) - 1]
        id_last_student = last_student.id
        fname_last_stud = last_student.fname
        sname_last_stud = last_student.sname
        s_list = self._ser.search_stud_id(id_last_student)
        for s in s_list:
            self.assertEqual(fname_last_stud, s[1])
            self.assertEqual(sname_last_stud, s[2])

        # test search stud entire name
        s_list = list()
        last_student = self._repo[len(self._repo) - 1]
        id_last_student = last_student.id
        fname_last_stud = last_student.fname
        sname_last_stud = last_student.sname
        s_list = self._ser.search_stud_ename(fname_last_stud, sname_last_stud)
        for s in s_list:
            self.assertEqual(id_last_student, s[0])

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