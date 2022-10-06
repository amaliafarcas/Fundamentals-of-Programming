class Discipline:
    """
    - discipline id, name
    """

    def __init__(self, _id, name):
        """
        Create a student
        :param _id:
        :param name
        """
        self.__id = _id
        self.__name = name

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return "Discipline id: " + str(self.id) + "   Name: " + str(self.name)


def test_discipline():
    dis = Discipline(100, "english")
    assert dis.id == 100
    assert dis.name == "english"


test_discipline()
