import os


def create(path_name):
    try:
        os.makedirs(path_name)
        return True
    except FileExistsError:
        # el directorio ya existe
        return True
    except Exception as e:
        return False


def exists(dir_name):
    return os.path.exists(dir_name)


def walk(path):
    resp = []
    for root, dirs, files in os.walk(path):
        resp.append({
            'root': root,
            'dirs': dirs,
            'files': files
        })
    return resp
