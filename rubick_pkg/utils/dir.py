import os

from rubick_pkg.context import pass_context
from rubick_pkg.responses import DIRECTORY_NOT_CREATED, SCAFFOLD_NOT_FOUND


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


def create_file_path(full_file_name):
    path = os.path.dirname(full_file_name)
    # create project
    if not create(path):
        raise Exception(DIRECTORY_NOT_CREATED % path)


@pass_context
def get_scaffold_dir(ctx, paths=[]):
    scaffold_dir = os.path.join(ctx.scaffolds_local, *paths)
    if not exists(scaffold_dir):
        raise Exception(SCAFFOLD_NOT_FOUND)
    return scaffold_dir
