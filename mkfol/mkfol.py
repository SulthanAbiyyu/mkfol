import sys
from rich.console import Console
from semester import make_semester_path
from ds_ml import make_ds_ml_path
from ds2 import make_ds2_ml2_path
from semester_week import make_mk_weekly_path
# import semester
# import ds_ml
# import ds2
# import semester_week

# Console for Rich Console
console = Console()


def mkfol():
    if len(sys.argv) <= 1:
        console.print(""" 
███╗░░░███╗██╗░░██╗███████╗░█████╗░██╗░░░░░
████╗░████║██║░██╔╝██╔════╝██╔══██╗██║░░░░░
██╔████╔██║█████═╝░█████╗░░██║░░██║██║░░░░░
██║╚██╔╝██║██╔═██╗░██╔══╝░░██║░░██║██║░░░░░
██║░╚═╝░██║██║░╚██╗██║░░░░░╚█████╔╝███████╗
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░╚════╝░╚══════╝                           
""", style="bold")
        console.print("Author : Sulthan Abiyyu Hakim\n", style="bold blue")
        console.print("[bold]Contributor :[/]\n- I Dewa Made (DewaMadeWira)", style="blue")
        print("\n")
        console.print("Type: [bold]'mkfol -h'[/] for more command. ")
        return

    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        console.print(
            """
            [bold green]Command List : [/] 🤖

            [bold]misc:[/]
            -h / --help : show this help
            -v / --version : show version

            [bold]main feature:[/]
            -s / --semester : make semester folder
            -ds / --datascience / -ml / --machinelearning : make ds_ml folder
            -ds2 / --datascience2 / -ml2 / --machinelearning2 : make ds 2 folder
            -w / --week
            
            [bold]usage:[/]
            mkfol -s <semester> "<mata kuliah (separate with comma)>"
            mkfol -w <semester> "<mata kuliah (separate with comma)>" <number of weeks>

            """
        )
        return

    if sys.argv[1] == "-v" or sys.argv[1] == "--version":
        print("mkfol version 1.0")
        return

    if sys.argv[1] == "-s" or sys.argv[1] == "--semester":
        try:
            semester = int(sys.argv[2])
            mata_kuliah = sys.argv[3]
            make_semester_path(mata_kuliah, semester)
            print("semester folder created")
        except Exception as error:
            if(str(error)== "list index out of range"):
                console.print("Input parameter missing !\n", style="bold red")
                console.print("Valid command are : \n[bold]mkfol -s 2 'lecture1,lecture2'[/]" )
            else : 
                print(error)
        return

    if sys.argv[1] == "-ds" or sys.argv[1] == "--datascience" or sys.argv[1] == "-ml" or sys.argv[1] == "--machinelearning":
        make_ds_ml_path()
        print("data science or machine learning project folder created")
        return

    if sys.argv[1] == "-ds2" or sys.argv[1] == "--datascience2" or sys.argv[1] == "-ml2" or sys.argv[1] == "--machinelearning2":
        make_ds2_ml2_path()
        print("data science 2 or machine learning 2 project folder created")

    if sys.argv[1] == "-w" or sys.argv[1] == "--week":
        try :
            semester = int(sys.argv[2])
            mata_kuliah = sys.argv[3]
            week = int(sys.argv[4])
            make_mk_weekly_path(mata_kuliah, semester, week)
        except Exception as error:
            if(str(error)== "list index out of range"):
                console.print("Input parameter missing !\n", style="bold red")
                console.print("Valid command are : \n[bold]mkfol -w 2 'lecture1,lecture2' 3[/]" )
            else : 
                print(error)

    else:
        print("Please enter valid arguments! mkfol -h for help")


if __name__ == "__main__":
    mkfol()
