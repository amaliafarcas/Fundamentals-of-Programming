from src.domain.student import Student


class StudVal:
    def __init__(self):
        self._stu = Student

    def validate(self, student):
        if student.id > 9999 or student.id < 1000:
            raise ValueError("Student id not valid")
        else:
            return True

    def validate_id(self, sid):
        if int(sid) > 9999 or int(sid) < 1000:
            raise ValueError("Student id is not valid")
        else:
            return True
