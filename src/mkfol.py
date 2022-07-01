import sys
from semester import make_semester_path


def mkfol():
    if len(sys.argv) <= 2:
        print("Usage: mkfol.py -h")
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
            mkfol.py -s <semester> <mata kuliah (separate with comma)>
            """
        )
        return

    if sys.argv[1] == "-v" or sys.argv[1] == "--version":
        print("mkfol.py version 0.1")
        return

    if sys.argv[1] == "-s" or sys.argv[1] == "--semester":
        semester = int(sys.argv[2])
        mata_kuliah = sys.argv[3]
        make_semester_path(mata_kuliah, semester)
        return

    print("Please enter valid arguments! mkfol.py -h for help")


if __name__ == "__main__":
    mkfol()
