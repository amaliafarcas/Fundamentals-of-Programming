from src.domain.discipline import Discipline
from src.domain.discipline_validator import DisVal
from random import randint
import unittest
from src.services.undo_service import Operation, Exception, CascadedOperation, FunctionCall
from src.services.gnome_sort import gnomeSort

class DisciplineSer:
    def __init__(self, discipline_repo, undo_service):
        self.__repo = discipline_repo
        self._validator = DisVal()
        self.name_list = ['english', 'programming', 'mathematics', 'logics', 'asc']
        self.__undo_service = undo_service

    def add_dis_undo(self, did, dname):
        """
        adds a discipline (undo/redo function)
        :param did: id
        :param dname: name
        :return:
        """
        dis = Discipline(did, dname)
        self.__repo.add_dis(dis)

    def add_dis(self, dis):
        """
        adds a discipline
        :param dis: discipline
        :return:
        """
        self._validator.validate(dis)
        self.__repo.add_dis(dis)

    def add_discipline(self, dis):
        """
        adds a new student
        :param dis: the student that needs to be added
        :return:
        """

        try:
            self._validator.validate(dis)
            self.__repo.add_dis(dis)
            fc_undo = FunctionCall(self.delete_dis, dis.id)
            fc_redo = FunctionCall(self.add_dis_undo, dis.id, dis.name)
            cope = CascadedOperation()
            cope.add(Operation(fc_undo, fc_redo))
            self.__undo_service.record_operation(cope)

        except Exception as ve:
            raise ve
        return dis

    def delete_discipline(self, d, n):
        """
        deletes a discipline
        :param d: id
        :param n: name
        :return:
        """
        dis = Discipline(d, n)
        self.__repo.delete_dis(dis)

    def delete_discipline_id(self, d):
        """
        deletes discipline by id
        :param d: id
        :return:
        """
        self.__repo.delete_dis_id(d)

    def delete_dis(self, dis_id):
        # TODO undo
        """
        deletes a discipline with a given id
        :param dis_id: the id of the discipline that needs to be removed
        :return:
        """
        discipline_list = self.__repo.show_dis()
        self._validator.validate_id(dis_id)
        k = 0
        i = 0
        s = 0
        while i < len(discipline_list):
            if int(discipline_list[i].id) == int(dis_id):
                s = discipline_list[i]
                k = 1
            i += 1
        if k == 0:
            raise Exception("No discipline to be removed (delete_dis  - serv)")
        else:
            self.__repo.delete_dis(s)

    def modify_dis(self, dis_id, n):
        """
        modifies a discipline (undo/redo function)
        :param dis_id: id
        :param n: new name
        :return:
        """
        self.__repo.mod_dis(dis_id, n)

    def mod_dis(self, dis_id, n):
        """
        modifies a discipline
        :param dis_id: id
        :param n: new name
        :return:
        """
        discipline_list = self.__repo.show_dis()
        on = 0
        k = 0
        i = 0
        while i < len(discipline_list):
            if int(discipline_list[i].id) == int(dis_id):
                on = discipline_list[i].name
                k = 1
            i += 1
        if k == 0:
            raise Exception("No discipline to be modified")
        else:
            try:
                self.__repo.mod_dis(dis_id, n)
                fc_undo = FunctionCall(self.modify_dis, dis_id, on)
                fc_redo = FunctionCall(self.modify_dis, dis_id, n)
                cope = CascadedOperation()
                cope.add(Operation(fc_undo, fc_redo))
                self.__undo_service.record_operation(cope)

            except Exception as ve:
                raise ve

    def generate_disciplines(self):
        """
        generates randomly a list of disciplines
        :return:
        """
        k = 310
        p = len(self.name_list)
        for i in range(p):
            d = k
            n = self.name_list[i]
            dis = Discipline(d, n)
            self.__repo.add_dis(dis)
            e = randint(1, 4)
            k = k + e

    def show_dis(self):
        """

        :return: the list of disciplines
        """
        return self.__repo.show_dis()

    def show_dis_len(self):
        """

        :return: the list of disciplines
        """
        listt = list()
        listt, le = self.__repo.show_dis_len()
        return listt, le

    def sort_dis(self):
        dis_list = self.__repo.show_dis()
        sorted_list = list()
        k = 0
        for s in dis_list:
            k = 1
            sorted_list.append([s.id, s.name])
        if k == 0:
            raise Exception("Discipline list is empty")
        else:
            return gnomeSort(sorted_list, len(sorted_list), 0)

    def is_discipline(self, did):
        """
        verifies if an id introduced by the user is in the discipline list
        :param did: the id that needs to be verified
        :return: True of False
        """
        dis = self.__repo.show_dis()
        k = 0
        for d in dis:
            if int(d.id) == int(did):
                k = 1
        if k == 0:
            raise Exception("No discipline with such id")
        else:
            return True

    def is_discipline_true(self, did):
        """
        verifies if an id introduced by the user is in the discipline list
        :param did: the id that needs to be verified
        :return: True of False
        """
        dis = self.__repo.show_dis()
        k = 0
        for d in dis:
            if int(d.id) == int(did):
                k = 1
        if k == 0:
            return False
        else:
            return True

    def is_dis_rem(self, did):
        """
        verifies if an id introduced by the user is in the discipline list
        :param did: the id that needs to be verified
        :return: True of False
        """
        dis = self.__repo.show_dis()
        k = 0
        for d in dis:
            if int(d.id) == int(did):
                k = 1
        if k == 0:
            raise Exception("No discipline to be removed")
        else:
            return True

    def search_dis_id(self, sid):
        """
        search for a discipline with a given id/partial id
        :param sid: the id/partial id introduced by the user
        :return: a list of the matching ids (and the discipline names)
        """
        dis_list = self.__repo.show_dis()
        k = 0
        d_list = list()
        for s in dis_list:
            if sid in str(s.id):
                k = 1
                d_list.append([s.id, s.name])
        if k == 0:
            raise Exception("No discipline with such id")
        else:
            return d_list

    def search_n_dis_id(self, sid):
        """
        search for a discipline with a given id/partial id
        :param sid: the id/partial id introduced by the user
        :return: a list of the matching ids (and the discipline names)
        """
        dis_list = self.__repo.show_dis()
        k = 0
        name = 0
        for s in dis_list:
            if sid in str(s.id):
                k = 1
                name = s.name
        if k == 0:
            raise Exception("No discipline with such id")
        else:
            return name

    def search_dis_name(self, name):
        """
        search for a discipline with a give name/partial name
        :param name: the name/partial name introduced by the user
        :return: a list of the matching names (and the discipline ids)
        """
        dis_list = self.__repo.show_dis()
        k = 0
        d_list = list()
        for s in dis_list:
            f = s.name
            if name.lower() in str(f).lower():
                d_list.append([s.id, s.name])
                k = 1
        if k == 0:
            raise Exception("No discipline with such name")
        else:
            return d_list


class DisciplineServTest(unittest.TestCase):
    def setup(self, discipline_repo, undo_service):
        """
        Runs before any of the tests
        Used to set up the class so that tests can be run

        :return: None
        """
        self._repo = discipline_repo
        self._ser = DisciplineSer(discipline_repo, undo_service)
        self._dis = Discipline(107, 'arts')
        self._repo.add_dis(self._dis)

    def test_repo_elem(self):
        # test add
        self.assertEqual(len(self._repo), 6)
        self._repo.add_dis(Discipline(425, 'economics'))
        self._repo.add_dis(Discipline(559, 'astronomy'))
        self.assertEqual(len(self._repo), 8)

        # test delete
        last_dis = self._repo[len(self._repo)-1]
        id_last_dis = last_dis.id
        self._repo.delete_dis(id_last_dis)
        self.assertEqual(len(self._repo), 7)

        # test update
        last_dis = self._repo[len(self._repo)-1]
        id_last_dis = last_dis.id
        self._repo.mod_dis(id_last_dis, "lala")
        last_dis = self._repo[len(self._repo) - 1]
        name_last_dis = last_dis.name
        self.assertEqual(name_last_dis, "lala")

        # test search stud id
        last_dis = self._repo[len(self._repo) - 1]
        id_last_dis = last_dis.id
        name_last_stud = last_dis.name
        s_list = self._ser.search_dis_id(id_last_dis)
        for s in s_list:
            self.assertEqual(name_last_stud, s[1])

        # test search stud entire name
        last_dis = self._repo[len(self._repo) - 1]
        id_last_dis = last_dis.id
        name_last_dis = last_dis.fname
        s_list = self._ser.search_dis_name(name_last_dis)
        for s in s_list:
            self.assertEqual(id_last_dis, s[0])

    def tearDown(self) -> None:
        """
        Runs after all the tests have completed
        Used to close the test environment (clase files, DB connections, deallocate memory)

        :return: None
        """
        self._repo = None
