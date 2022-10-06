from src.domain.grade import Grade
import unittest
import pickle
from src.repository.iterable_structure import IterableStructure


class Repograde:
    def __init__(self):
        self.__data = IterableStructure()

    def add_gr(self, gr):
        """
        adds a new grade
        :param gr: the grade that needs to be added
        :return:
        """
        self.__data.append(gr)

    def add_grade(self, sid, did, gr):
        """
        adds a grade
        :param sid:
        :param did:
        :param gr:
        :return:
        """
        grade = Grade(sid, did, gr)
        self.__data.append(grade)

    def add_mult_grades(self, deleted_list):
        """
        adds multiple grades
        :param deleted_list: the list of grades that have to be added
        :return:
        """
        for gr in deleted_list:
            self.__data.append(gr)

    def delete_mult_grades(self, deleted_list):
        """
        deleted multiple grades
        :param deleted_list: the list of grades that have to be deleted
        :return:
        """
        i = 0
        while i < len(self.__data):
            for gr in deleted_list:
                if self.__data[i] == gr:
                    self.__data.__delitem__(i)
                    i -= 1
            i += 1

    def delete_grade(self, sid, did, gr):
        """
        deletes a grade
        :param sid: student id
        :param did: discipline id
        :param gr: grade
        :return:
        """
        grade = Grade(sid, did, gr)
        q = 0
        i = 0
        while i < len(self.__data):
            if self.__data[i] == grade:
                q = i
            i += 1
        self.__data.__delitem__(q)

    def delete_gr(self, gr):
        """
        deletes a grade
        :param gr: the grade that needs to be deleted
        :return:
        """
        q = 0
        i = 0
        while i < len(self.__data):
            if self.__data[i] == gr:
                q = i
            i += 1
        self.__data.__delitem__(q)

    def mod_grade(self, ds, di, o, gr):
        """
        modifies a given grade
        :param ds: student id
        :param di: discipline id
        :param o: old grade
        :param gr: new grade
        :return:
        """
        for i in range(0, len(self.__data)):
            if int(self.__data[i].stud_id) == int(ds) and int(self.__data[i].dis_id) == int(di)\
                    and int(self.__data[i].grade) == int(o):
                self.__data[i].grade = gr

    def show_grade(self):
        """

        :return: the list of grades
        """
        temp = []
        for i in range(0, len(self.__data)):
            temp.append(self.__data[i])
        return temp

    def show_grade_len(self):
        """

        :return: the list of students
        """
        temp = []
        for i in range(0, len(self.__data)):
            temp.append(self.__data[i])
        return temp, len(self.__data)

    def set_list(self, data):
        i = 0
        k = len(data)
        while i < k:
            stud = data[i]
            self.__data.append(stud)
            i += 1
        return self.__data


class GradeRepoTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testStudentRepositoryTest(self):
        repo = Repograde()
        tsr = [Grade(2000, 520, 9), Grade(2001, 214, 6), Grade(2003, 665, 10)]
        delete_list = [Grade(2000, 580, 10), Grade(2001, 914, 4), Grade(2003, 165, 5)]
        for i in range(0, len(tsr)):
            repo.add_gr(tsr[i])
        repo.add_gr(Grade(2005, 558, 9))
        tsr, l = repo.show_grade_len()
        self.assertEqual(tsr[3].stud_id, 2005)
        self.assertEqual(tsr[3].dis_id, 558)
        self.assertEqual(tsr[3].grade, 9)
        self.assertEqual(l, 4)

        repo.add_grade(2007, 667, 7)
        tsr, l = repo.show_grade_len()
        self.assertEqual(tsr[4].stud_id, 2007)
        self.assertEqual(tsr[3].dis_id, 667)
        self.assertEqual(tsr[3].grade, 7)
        self.assertEqual(l, 5)

        repo.add_mult_grades(delete_list)
        tsr, l = repo.show_grade_len()
        self.assertEqual(l, 8)

        repo.delete_gr(Grade(2003, 665, 10))
        tsr, l = repo.show_grade_len()
        self.assertEqual(l, 7)

        repo.delete_mult_grades(delete_list)
        tsr, l = repo.show_grade_len()
        self.assertEqual(l, 4)

        repo.delete_grade(2000, 520, 9)
        tsr, l = repo.show_grade_len()
        self.assertEqual(l, 3)

        repo.mod_grade(2001, 214, 6, 10)
        tsr, l = repo.show_grade_len()
        self.assertEqual(tsr[0].grade, 10)


class GradeFileTextRepo(Repograde):
    def __init__(self):
        super().__init__()
        self.text_file = "grade.txt"
        self.load_file()

    def load_file(self):
        with open(self.text_file, "r") as f:
            for line in f.readlines():
                line = line.strip()
                line = line.replace("\n", "")
                if len(line) > 1:
                    stud_id, dis_id, grade = line.split(",", maxsplit=2)
                    gr = Grade(stud_id, dis_id, grade)
                    self.add_gr(gr)

    def save_file(self):
        with open(self.text_file, "w") as f:
            gr_list = self.show_grade()
            for gr in gr_list:
                f.write(str(gr.stud_id) + "," + str(gr.dis_id) + "," + str(gr.grade) + "\n")

    def add_gr(self, gr):
        super(GradeFileTextRepo, self).add_gr(gr)
        self.save_file()

    def add_grade(self, sid, did, gr):
        super(GradeFileTextRepo, self).add_grade(sid, did, gr)
        self.save_file()

    def add_mult_grades(self, deleted_list):
        super(GradeFileTextRepo, self).add_mult_grades(deleted_list)
        self.save_file()

    def delete_grade(self, sid, did, gr):
        aux = super(GradeFileTextRepo, self).delete_grade(sid, did, gr)
        self.save_file()
        return aux

    def delete_mult_grades(self, deleted_list):
        aux = super(GradeFileTextRepo, self).delete_mult_grades(deleted_list)
        self.save_file()
        return aux

    def mod_grade(self, ds, di, o, gr):
        super(GradeFileTextRepo, self).mod_grade(ds, di, o, gr)
        self.save_file()


class GradeFileBinRepo(Repograde):
    def __init__(self):
        super().__init__()
        self.text_file = "grade.bin"
        self._load_file()

    def _load_file(self):
        with open(self.text_file, "rb") as f:
            try:
                self.data = pickle.load(f)
                self.set_list(self.data)
            except EOFError:
                self.data = list()

    def _save_file(self):
        with open(self.text_file, "wb") as f:
            self.data = self.show_grade()
            pickle.dump(self.data, f)

    def add_gr(self, gr):
        super(GradeFileBinRepo, self).add_gr(gr)
        self._save_file()

    def add_grade(self, sid, did, gr):
        super(GradeFileBinRepo, self).add_grade(sid, did, gr)
        self._save_file()

    def add_mult_grades(self, deleted_list):
        super(GradeFileBinRepo, self).add_mult_grades(deleted_list)
        self._save_file()

    def delete_grade(self, sid, did, gr):
        aux = super(GradeFileBinRepo, self).delete_grade(sid, did, gr)
        self._save_file()
        return aux

    def delete_mult_grades(self, deleted_list):
        aux = super(GradeFileBinRepo, self).delete_mult_grades(deleted_list)
        self._save_file()
        return aux

    def mod_grade(self, ds, di, o, gr):
        super(GradeFileBinRepo, self).mod_grade(ds, di, o, gr)
        self._save_file()
