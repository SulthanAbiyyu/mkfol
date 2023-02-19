import os


def make_mk_weekly_path(mata_kuliah: str, semester: int, n_weeks: int = 16):
    current_path = os.getcwd()
    path = os.path.join(current_path, f"semester {semester}")
    os.mkdir(path)
    mata_kuliahs = mata_kuliah.split(",")

    current_path = path
    for mata_kuliah in mata_kuliahs:
        path = os.path.join(current_path, mata_kuliah)
        os.mkdir(path)

        current_current_path = path
        for week in range(n_weeks):
            content = f"week {week + 1}"
            path_path = os.path.join(current_current_path, content)
            os.mkdir(path_path)
