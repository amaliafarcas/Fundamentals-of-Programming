import pickle
import unittest
from src.domain.student import Student
from src.repository.iterable_structure import IterableStructure


class StudentRepo:
    def __init__(self):
        self.__data = IterableStructure()

    def add_student(self, stud):
        """
        adds a new student
        :param stud: the student
        :return:
        """
        self.__data.append(stud)

    def add_st(self, sid, fn, sn):
        stud = Student(sid, fn, sn)
        self.__data.append(stud)

    def delete_stud(self, s):
        """
        deletes a student
        :param s: the stud
        :return:
        """
        q = -1
        for i in range(0, len(self.__data)):
            if int(self.__data[i].id) == int(s.id):
                q = i
        if q != -1:
            self.__data.__delitem__(q)
            return True
        else:
            raise Exception("Invalid id")

    def delete_stud_id(self, s):
        """
        deletes a student by a given id
        :param s: student s id
        :return:
        """
        q = -1
        for i in range(0, len(self.__data)):
            if int(self.__data[i].id) == int(s):
                q = i
        if q != -1:
            self.__data.__delitem__(q)
            return True
        else:
            raise Exception("Invalid id")

    def mod_stud(self, s, nf, ns):
        """
        modifies a student with a given id
        :param s: the student that need to be modified
        :param nf: new first name
        :param ns: new old name
        :return:
        """
        for i in range(0, len(self.__data)):
            if self.__data[i].id == int(s):
                self.__data[i].fname = nf
                self.__data[i].sname = ns

    def show_stud(self):
        """

        :return: the list of students
        """
        temp = []
        for i in range(0, len(self.__data)):
            temp.append(self.__data[i])
        return temp

    def show_stud_len(self):
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


class StRepoTest(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testStudentRepositoryTest(self):
        repo = StudentRepo()
        tsr = [Student(2000, "Ana", "Molnar"), Student(2001, "Edi", "Mircea"), Student(2003, "Radita", "Vancea")]
        for i in range(0, len(tsr)):
            repo.add_student(tsr[i])
        repo.add_student(Student(2005, "Baican", "Victor"))
        tsr, l = repo.show_stud_len()
        self.assertEqual(tsr[3].id, 2005)
        self.assertEqual(tsr[3].fname, "Baican")
        self.assertEqual(tsr[3].sname, "Victor")
        self.assertEqual(l, 4)

        repo.add_st(2007, "Baican", "Mara")
        tsr, l = repo.show_stud_len()
        self.assertEqual(tsr[4].id, 2007)
        self.assertEqual(tsr[3].fname, "Baican")
        self.assertEqual(tsr[3].sname, "Mara")
        self.assertEqual(l, 5)

        repo.delete_stud(Student(2003, "Radita", "Vancea"))
        tsr, l = repo.show_stud_len()
        self.assertEqual(l, 4)
        self.assertEqual(repo.delete_stud_id(Student(2005, "Baican", "Victor")), True)
        repo.mod_stud(2000, "Valeriu", "Cipri")
        tsr, l = repo.show_stud_len()
        self.assertEqual(tsr[0].fname, "Valeriu")
        self.assertEqual(tsr[0].sname, "Cipri")


class StudentFileTextRepo(StudentRepo):
    def __init__(self):
        super().__init__()
        self.text_file = "students.txt"
        self.load_file()

    def load_file(self):
        with open(self.text_file, "r") as f:
            for line in f.readlines():
                line = line.strip()
                line = line.replace("\n", "")
                if len(line) > 1:
                    stud_id, stud_fname, stud_sname = line.split(",", maxsplit=2)
                    stud = Student(stud_id, stud_fname, stud_sname)
                    self.add_student(stud)

    def save_file(self):
        with open(self.text_file, "w") as f:
            stud_list = self.show_stud()
            for stud in stud_list:
                f.write(str(stud.id) + "," + str(stud.fname) + "," + str(stud.sname) + "\n")

    def add_student(self, stud):
        super(StudentFileTextRepo, self).add_student(stud)
        self.save_file()

    def delete_stud(self, stud):
        aux = super(StudentFileTextRepo, self).delete_stud(stud)
        self.save_file()
        return aux

    def delete_stud_id(self, stud):
        aux = super(StudentFileTextRepo, self).delete_stud_id(stud)
        self.save_file()
        return aux

    def mod_stud(self, s, nf, ns):
        super(StudentFileTextRepo, self).mod_stud(s, nf, ns)
        self.save_file()


class StudentFileBinRepo(StudentRepo):
    def __init__(self):
        super().__init__()
        self.text_file = "students.bin"
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
            self.data = self.show_stud()
            pickle.dump(self.data, f)

    def add_student(self, stud):
        super(StudentFileBinRepo, self).add_student(stud)
        self._save_file()

    def delete_stud(self, stud):
        aux = super(StudentFileBinRepo, self).delete_stud(stud)
        self._save_file()
        return aux

    def delete_stud_id(self, stud):
        aux = super(StudentFileBinRepo, self).delete_stud_id(stud)
        self._save_file()
        return aux

    def mod_stud(self, s, nf, ns):
        super(StudentFileBinRepo, self).mod_stud(s, nf, ns)
        self._save_file()
