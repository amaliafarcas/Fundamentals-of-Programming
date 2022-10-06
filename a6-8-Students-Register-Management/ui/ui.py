from src.services.sudent_service import StudentService
from src.services.grade_service import GradeSer
from src.services.dis_serv import DisciplineSer
from src.domain.student import Student
from src.domain.discipline import Discipline
from src.domain.grade import Grade
from random import randint
from src.repository.repository_exception import Exception


class Ui:
    def __init__(self, student_service, grade_service, discipline_service, undo_service):
        self.__studService = student_service
        self.__gradeService = grade_service
        self.__disService = discipline_service
        self._studfunc = StudentService(self.__studService, undo_service)
        self._gradefunc = GradeSer(self.__gradeService, self.__studService, self.__disService, undo_service)
        self._disfunc = DisciplineSer(self.__disService, undo_service)
        self.__undo_service = undo_service

    def add_student(self, k):
        while self.__studService.is_student_true(k) == True:
            k += 1
        print("Student's first name: ")
        f = input()
        print("Student's second name: ")
        s = input()
        stud = Student(k, f, s)
        self.__studService.add_stud(stud)

    def delete_student(self):
        try:
            print("Enter student id: ")
            stud_id = input()
            self.__studService.is_student_rem(stud_id)
            self.__gradeService.delete_studgrade(stud_id)
            self.__studService.delete_stud(stud_id)
        except Exception as ve:
            print(str(ve))

    def modify_student(self):
        try:
            print("Enter student id: ")
            stud_id = input()
            print("Enter student's first name: ")
            new_fname = input()
            print("Enter student's second name: ")
            new_sname = input()
            self.__studService.mod_stud(stud_id, new_fname, new_sname)
        except Exception as ve:
            print(str(ve))

    def _print_students(self):
        i = 0
        try:
            students = self.__studService.sort_stud()
            for el in students:
                print("Student id:", el[0], "   Name: ", el[1], el[2])
                i += 1
        except Exception as ve:
            print(str(ve))

    def add_discipline(self, k):
        while self.__disService.is_discipline_true(k) == True:
            k += 1
        print("Discipline name: ")
        f = input()
        dis = Discipline(k, f)
        self.__disService.add_discipline(dis)

    def delete_discipline(self):
        try:
            print("Enter discipline id: ")
            dis_id = input()
            self.__disService.is_dis_rem(dis_id)
            self.__gradeService.delete_disgrade(dis_id)
            self.__disService.delete_dis(dis_id)
        except Exception as ve:
            print(str(ve))

    def modify_discipline(self):
        try:
            print("Enter discipline id: ")
            stud_id = input()
            print("Enter discipline name: ")
            new_name = input()
            self.__disService.mod_dis(stud_id, new_name)
        except Exception as ve:
            print(str(ve))

    def _print_disciplines(self):
        i = 0
        discipline = self.__disService.sort_dis()
        try:
            while i < len(discipline):
                print("Discipline id:", discipline[i][0], "   Name: ", discipline[i][1])
                i += 1
        except Exception as ve:
            print(str(ve))

    def add_grade(self):
        try:
            print("Student id: ")
            s = input()
            print("Discipline id: ")
            d = input()
            print("Grade: ")
            gr = input()
            grade = Grade(s, d, gr)
            self.__gradeService.add_grade(grade)
        except Exception as ve:
            print(str(ve))

    def delete_grade(self):
        try:
            print("Student id: ")
            s = input()
            print("Discipline id: ")
            d = input()
            print("Grade: ")
            g = input()
            self.__gradeService.delete_grade(s, d, g)
        except Exception as ve:
            print(str(ve))

    def modify_grade(self):
        try:
            print("Student id: ")
            s = input()
            print("Discipline id: ")
            d = input()
            print("Old grade: ")
            o = input()
            print("New grade: ")
            n = input()
            self.__gradeService.mod_grade(s, d, o, n)
        except Exception as ve:
            print(str(ve))

    def _print_grade(self):
        i = 0
        grades = self.__gradeService.sort_gr()
        try:
            while i < len(grades):
                print("Student id:", grades[i][0], "   Discipline id: ", grades[i][1], " Grade:", grades[i][2])
                i += 1
        except Exception as ve:
            print(str(ve))

    def search_stud_id(self):
        try:
            print("Enter student id: ")
            sid = input()
            slist = self.__studService.search_stud_id(sid)
            for el in slist:
                print("Student id", el[0], "name:", el[1], el[2])
        except Exception as ve:
            print(str(ve))

    def search_stud_partname(self):
        try:
            print("Enter student name: ")
            name = input()
            slist = self.__studService.search_stud_pname(name)
            for el in slist:
                print("Student id", el[0], "name:", el[1], el[2])
        except Exception as ve:
            print(str(ve))

    def search_stud_entirename(self):
        try:
            print("Enter first name: ")
            fname = input()
            print("Enter second name: ")
            sname = input()
            slist = self.__studService.search_stud_ename(fname, sname)
            for el in slist:
                print("Student id", el[0], "name:", el[1], el[2])
        except Exception as ve:
            print(str(ve))

    def search_dis_id(self):
        try:
            print("Enter discipline id: ")
            sid = input()
            slist = self.__disService.search_dis_id(sid)
            for el in slist:
                print("Discipline id:", el[0], "name:", el[1])
        except Exception as ve:
            print(str(ve))

    def search_dis_name(self):
        try:
            print("Enter discipline name: ")
            name = input()
            slist = self.__disService.search_dis_name(name)
            for el in slist:
                print("Discipline id:", el[0], "name:", el[1])
        except Exception as ve:
            print(str(ve))

    def students_failing(self):
        slist = self.__gradeService.students_failing()
        if len(slist) != 0:
            k = 0
            for el in slist:
                if el[0] != k:
                    k = el[0]
                    print("\nStudent with id", el[0], "name", el[1], el[2], "\nis failing at", el[3], el[4])
                else:
                    print("and", el[3], el[4])
        else:
            print("No students failing")

    def best_students(self):
        slist = self.__gradeService.best_students()
        if len(slist) != 0:
            for el in slist:
                print("Stundent id", el[0], "name", el[1], el[2], "has total average", el[3])
        else:
            print("No good students")

    def discipline_average(self):
            try:
                slist = self.__gradeService.discipline_average()
                for el in slist:
                    print("Discipline id", el[0], "name", el[1], "average", el[2])
            except Exception as ve:
                print(str(ve))

    def undo(self):
        try:
            self.__undo_service.undo()
        except Exception as ve:
            print(str(ve))

    def redo(self):
        try:
            self.__undo_service.redo()
        except Exception as ve:
            print(str(ve))

    def print_menu(self):
        print("\n1. Show students")
        print("2. Add student")
        print("3. Delete student based on id")
        print("4. Update student name by id")
        print("\t5. Show disciplines")
        print("\t6. Add discipline")
        print("\t7. Delete discipline based on id")
        print("\t8. Update discipline name by id")
        print("9. Show all grades")
        print("10. Add grade")
        print("11. Delete grade")
        print("12. Update grade")
        print("\t13. Search student by id")
        print("\t14. Search student by name")
        print("15. Search discipline by id")
        print("16. Search discipline by name")
        print("\t17. Students failing")
        print("\t18. Best students")
        print("\t19. Discipline average")
        print("20. Undo")
        print("21. Redo")
        print("22. Exit\n")

    def menu_search_student(self):
        print("1. Search by entire name")
        print("2. Search by partial/one name")

    def start(self):

        filetype = settings_properties()
        if filetype == "in memory":
            self._studfunc.generate_students(5)
            self._disfunc.generate_disciplines()
            self._gradefunc.generate_grades()

        k = 2000
        a = 400
        while True:
            try:
                self.print_menu()
                print("Insert option: ")
                option = input()
                if option == '1':
                    self._print_students()
                if option == '2':
                    self.add_student(k)
                    e = randint(1, 4)
                    k = k + e
                if option == '3':
                    self.delete_student()
                if option == '4':
                    self.modify_student()
                if option == '5':
                    self._print_disciplines()
                if option == '6':
                    self.add_discipline(a)
                    e = randint(1, 4)
                    a = a + e
                if option == '7':
                    self.delete_discipline()
                if option == '8':
                    self.modify_discipline()
                if option == '9':
                    self._print_grade()
                if option == '10':
                    self.add_grade()
                if option == '11':
                    self.delete_grade()
                if option == '12':
                    self.modify_grade()
                if option == '13':
                    self.search_stud_id()
                if option == '14':
                    self.menu_search_student()
                    print("Input option: ")
                    op = input()
                    if op == "1":
                        self.search_stud_entirename()
                    elif op == "2":
                        self.search_stud_partname()
                    else:
                        print("Invalid option")
                if option == '15':
                    self.search_dis_id()
                if option == '16':
                    self.search_dis_name()
                if option == '17':
                    self.students_failing()
                if option == '18':
                    self.best_students()
                if option == '19':
                    self.discipline_average()
                if option == '20':
                    self.undo()
                if option == '21':
                    self.redo()
                if option == '22':
                    return
                if int(option) < 1 or int(option) > 22:
                    print("Invalid option")
            except ValueError as ve:
                print(str(ve))


def settings_properties():
    file_name = "settings.properties"

    with open(file_name, "r") as f:
        line = f.readline()
        line = line.strip("\n")
        rep, filetype = line.split("=")

    return filetype
