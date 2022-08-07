import os

def find(path="."):
    if path == ".":
        path = os.getcwd()

    python_files = []

    for root, dirs, files in os.walk(path):
        for _file in files:
            if _file.endswith(".py"):
                python_files.append(os.path.join(root, _file))

    return python_files
