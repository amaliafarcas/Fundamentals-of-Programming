from src.domain.discipline import Discipline
import unittest
import pickle
from src.repository.iterable_structure import IterableStructure


class DisRepo:
    def __init__(self):
        self.__data = IterableStructure()

    def add_dis(self, dis):
        """
        adds a discipline
        :param dis: the discipline
        :return:
        """
        self.__data.append(dis)

    def delete_dis(self, d):
        """
        deletes a discipline
        :param d: the discipline
        :return:
        """
        q = 0
        i = 0
        while i < len(self.__data):
            if self.__data[i] == d:
                q = i
            i += 1
        self.__data.__delitem__(q)

    def delete_dis_id(self, d):
        """
        deletes a discipline with a given id
        :param d: the id
        :return:
        """
        q = -1
        for i in range(0, len(self.__data)):
            if int(self.__data[i].id) == int(d):
                q = i
        if q != -1:
            self.__data.__delitem__(q)
            return True
        else:
            raise Exception("Invalid id")

    def mod_dis(self, d, n):
        """
        modifies the name of a discipline with a given id
        :param d: the id of the discipline that has to be modified
        :param n: the new name of the discipline
        :return:
        """
        for i in range(0, len(self.__data)):
            if self.__data[i].id == int(d):
                self.__data[i].name = n

    def show_dis(self):
        """

        :return: the list of disciplines
        """
        temp = []
        for i in range(0, len(self.__data)):
            temp.append(self.__data[i])
        return temp

    def show_dis_len(self):
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
        repo = DisRepo()
        tsr = [Discipline(2000, "math"), Discipline(2001, "sports"), Discipline(2003, "arts")]
        for i in range(0, len(tsr)):
            repo.add_dis(tsr[i])
        repo.add_dis(Discipline(2005, "english"))
        tsr, l = repo.show_dis_len()
        self.assertEqual(tsr[3].id, 2005)
        self.assertEqual(tsr[3].name, "english")
        self.assertEqual(l, 4)

        repo.delete_dis(Discipline(2003, "arts"))
        tsr, l = repo.show_dis_len()
        self.assertEqual(l, 4)
        self.assertEqual(repo.delete_dis_id(Discipline(2005, "english")), True)
        repo.mod_dis(2000, "asc")
        tsr, l = repo.show_dis_len()
        self.assertEqual(tsr[0].name, "asc")


class DisciplineFileTextRepo(DisRepo):
    def __init__(self):
        super().__init__()
        self.text_file = "discipline.txt"
        self.load_file()

    def load_file(self):
        with open(self.text_file, "r") as f:
            for line in f.readlines():
                line = line.strip()
                line = line.replace("\n", "")
                if len(line) > 1:
                    dis_id, dis_name = line.split(",", maxsplit=1)
                    dis = Discipline(dis_id, dis_name)
                    self.add_dis(dis)

    def save_file(self):
        with open(self.text_file, "w") as f:
            dis_list = self.show_dis()
            for dis in dis_list:
                f.write(str(dis.id) + "," + str(dis.name) + "\n")

    def add_dis(self, dis):
        super(DisciplineFileTextRepo, self).add_dis(dis)
        self.save_file()

    def delete_dis(self, dis):
        aux = super(DisciplineFileTextRepo, self).delete_dis(dis)
        self.save_file()
        return aux

    def delete_dis_id(self, dis):
        aux = super(DisciplineFileTextRepo, self).delete_dis_id(dis)
        self.save_file()
        return aux

    def mod_dis(self, s, n):
        super(DisciplineFileTextRepo, self).mod_dis(s, n)
        self.save_file()


class DisciplineFileBinRepo(DisRepo):
    def __init__(self):
        super().__init__()
        self.text_file = "discipline.bin"
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
            self.data = self.show_dis()
            pickle.dump(self.data, f)

    def add_dis(self, dis):
        super(DisciplineFileBinRepo, self).add_dis(dis)
        self._save_file()

    def delete_dis(self, dis):
        aux = super(DisciplineFileBinRepo, self).delete_dis(dis)
        self._save_file()
        return aux

    def delete_dis_id(self, dis):
        aux = super(DisciplineFileBinRepo, self).delete_dis_id(dis)
        self._save_file()
        return aux

    def mod_dis(self, s, n):
        super(DisciplineFileBinRepo, self).mod_dis(s, n)
        self._save_file()
