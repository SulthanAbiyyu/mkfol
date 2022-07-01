import os

def make_semester_path(mata_kuliah: str, semester: int):
    current_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_path, f"semester {semester}")
    os.mkdir(path)
    mata_kuliahs = mata_kuliah.split(",")
    contents = ["1. tugas", "0. materi",
                "2. quiz", "3. UTS", "4. UAS", "lain-lain"]

    current_path = path
    for mata_kuliah in mata_kuliahs:
        path = os.path.join(current_path, mata_kuliah)
        os.mkdir(path)

        current_current_path = path
        for content in contents:
            path_path = os.path.join(current_current_path, content)
            os.mkdir(path_path)
