from src.services.sudent_service import StudentService
from src.services.grade_service import GradeSer
from src.services.dis_serv import DisciplineSer
from src.ui.ui import Ui
from src.services.undo_service import UndoCtrl
from src.repository.student_repo import StudentRepo, StudentFileTextRepo, StudentFileBinRepo
from src.repository.discipline_repo import DisRepo, DisciplineFileTextRepo, DisciplineFileBinRepo
from src.repository.repo_grade import Repograde, GradeFileTextRepo, GradeFileBinRepo


def settings_properties():
    file_name = "settings.properties"
    stud_repo = None
    dis_repo = None
    gr_repo = None

    with open(file_name, "r") as f:

        line = f.readline()
        line = line.strip("\n")
        repo, filetype = line.split("=")

        if filetype == 'text':

            for line in f.readlines():
                line = line.strip()
                line = line.strip("\n")

                repo, name = line.split("=")
                if repo == "student_file":
                    stud_repo = StudentFileTextRepo()
                elif repo == "discipline_file":
                    dis_repo = DisciplineFileTextRepo()
                elif repo == "grade_file":
                    gr_repo = GradeFileTextRepo()

        elif filetype == 'binary':

            for line in f.readlines():
                line = line.strip()
                line = line.strip("\n")

                repo, name = line.split("=")
                if repo == "student_file":
                    stud_repo = StudentFileBinRepo()
                elif repo == "discipline_file":
                    dis_repo = DisciplineFileBinRepo()
                elif repo == "grade_file":
                    gr_repo = GradeFileBinRepo()

        elif filetype == "in memory":
            stud_repo = StudentRepo()
            dis_repo = DisRepo()
            gr_repo = Repograde()

    return stud_repo, dis_repo, gr_repo


student_repo, discipline_repo, grade_repo = settings_properties()


# 2. Start the service to work with the selected repository
undo_service = UndoCtrl()
student_service = StudentService(student_repo, undo_service)
discipline_service = DisciplineSer(discipline_repo, undo_service)
grade_service = GradeSer(grade_repo, student_service, discipline_service, undo_service)

# 3. Start the UI with the initialized services
ui = Ui(student_service, grade_service, discipline_service, undo_service)

# 4. Start the program
ui.start()
