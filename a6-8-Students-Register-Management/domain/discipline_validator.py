from src.domain.discipline import Discipline
from src.repository.discipline_repo import DisRepo


class DisVal:
    def __init__(self):
        self._dis = Discipline
        self.__repo = DisRepo

    def validate(self, discipline):
        if discipline.id > 999 or discipline.id < 100:
            raise ValueError("Discipline id not valid")
        else:
            return True

    def validate_id(self, did):
        if int(did) > 999 or int(did) < 100:
            raise ValueError("Discipline id is not valid")
        else:
            return True
