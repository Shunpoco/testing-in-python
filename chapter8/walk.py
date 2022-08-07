import os

def find(path=".", _walk=None):
    _walk = _walk or os.walk
    if path == ".":
        path = os.getcwd()

    python_files = []

    for root, dirs, files in _walk(path):
        for _file in files:
            if _file.endswith(".py"):
                python_files.append(os.path.join(root, _file))

    return python_files
