import sys
from .semester import make_semester_path
from .ds_ml import make_ds_ml_path


def mkfol():
    if len(sys.argv) <= 1:
        print("Usage: mkfol -h")
        return

    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(
            """
            misc:
            -h / --help : show this help
            -v / --version : show version

            main feature:
            -s / --semester : make semester folder
            
            usage:
            mkfol -s <semester> <mata kuliah (separate with comma)>
            """
        )
        return

    if sys.argv[1] == "-v" or sys.argv[1] == "--version":
        print("mkfol version 1.0")
        return

    if sys.argv[1] == "-s" or sys.argv[1] == "--semester":
        semester = int(sys.argv[2])
        mata_kuliah = sys.argv[3]
        make_semester_path(mata_kuliah, semester)
        print("semester folder created")
        return

    if sys.argv[1] == "-ds" or sys.argv[1] == "--datascience" or sys.argv[1] == "-ml" or sys.argv[1] == "--machinelearning":
        make_ds_ml_path()
        print("data science or machine learning project folder created")
        return

    print("Please enter valid arguments! mkfol -h for help")


if __name__ == "__main__":
    mkfol()
