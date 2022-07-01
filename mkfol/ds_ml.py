import os


def make_ds_ml_path():
    dirs = ["data", "notebook", "src"]
    current_path = os.getcwd()

    for idx, dir in enumerate(dirs):
        path = os.path.join(current_path, dir)
        os.mkdir(path)
        if idx == 0:
            data_path = ["raw", "processed"]
            current_current_path = path
            for data_dir in data_path:
                path_path = os.path.join(current_current_path, data_dir)
                os.mkdir(path_path)

        if idx == 1:
            notebook_path = ["EDA", "modeling"]
            current_current_path = path
            for notebook_dir in notebook_path:
                path_path = os.path.join(current_current_path, notebook_dir)
                os.mkdir(path_path)

        if idx == 2:
            files = ["main.py", "train.py", "dataset.py",
                     "features.py", "visualization.py"]
            current_current_path = path
            for file in files:
                f = open(os.path.join(current_current_path, file), "x")
                f.close()

    other_files = ["README.md", "LICENSE", "requirements.txt", ".gitignore"]
    for file in other_files:
        f = open(os.path.join(current_path, file), "x")
        f.close()
