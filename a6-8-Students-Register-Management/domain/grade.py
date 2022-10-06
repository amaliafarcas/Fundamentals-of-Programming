class Grade:
    def __init__(self, stud_id, dis_id, grade):
        self._stud_id = stud_id
        self._dis_id = dis_id
        self._grade = grade

    @property
    def stud_id(self):
        return self._stud_id

    @property
    def dis_id(self):
        return self._dis_id

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "Student:" + str(self.stud_id) + "  Discipline:" + str(self.dis_id) + "  Grade:" + str(self.grade)
