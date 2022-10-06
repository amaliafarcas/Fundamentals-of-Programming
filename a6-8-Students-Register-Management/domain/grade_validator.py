from src.domain.student_validator import StudVal
from src.domain.discipline_validator import DisVal
from src.domain.grade import Grade


class GradeVal:
    def __init__(self):
        self._vals = StudVal
        self._vald = DisVal
        self._grade = Grade

    def validate(self, grade):
        if int(grade.grade) < int(0) or int(grade.grade) > int(10):
            raise ValueError("Invalid grade")
        else:
            return True
