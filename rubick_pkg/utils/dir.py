import os


def create(path_name):
    try:
        os.makedirs(path_name)
    except Exception as e:
        pass


def exists(dir_name):
    return os.path.isdir(dir_name) and os.path.exists(dir_name)
