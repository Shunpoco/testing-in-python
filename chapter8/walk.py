import os

def walk(path):
    for root, dirs, files in os.walk(path):
        for _file in files:
            yield os.path.join(root, _file)

def find(path=".", _walk=None):
    _walk = _walk or os.walk
    if path == ".":
        path = os.getcwd()

    python_files = []

    for _file in _walk(path):
        if _file.endswith(".py"):
            python_files.append(_file)

    return python_files
