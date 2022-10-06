class Student:
    """
    - stud id, name
    """

    def __init__(self, _id, fname, sname):
        """
        Create a student
        :param _id:
        :param sname:
        """
        self.__id = _id
        self.__fname = fname
        self.__sname = sname

    @property
    def id(self):
        return self.__id

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname

    @property
    def sname(self):
        return self.__sname

    @sname.setter
    def sname(self, sname):
        self.__sname = sname


def test_student():
    stud = Student(1001, "Far", "Ama")
    assert stud.id == 1001
    assert stud.fname == "Far"


test_student()
