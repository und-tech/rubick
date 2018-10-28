import os
import yaml
import json

from jinja2 import Template
from jinja2.utils import concat


def read(file_path):
    try:
        return open(file_path, 'r').read()
    except Exception:
        return False


def read_yml(file_path):
    try:
        return yaml.load(read(file_path))
    except Exception:
        raise Exception('No se pudo abrir el archivo YAML: %s' % file_path)


def read_json(file_path):
    try:
        return json.load(open(file_path))
    except Exception:
        raise Exception('No se pudo abrir el archivo JSON: %s' % file_path)


def create(file_name, template_content=None, **kwargs):
    f = open(file_name, "w+")
    if template_content is not None:
        template = Template(template_content)
        content = template.render(**kwargs)
        f.write(content)
    f.close()
    is_bash(file_name)


def append(file_path, content):
    with open(file_path, 'a') as f:
        f.write(content)


def get_template_block(file_path, block, **kwargs):
    template = Template(read(file_path))
    context = template.new_context(vars=kwargs)
    return concat(template.blocks[block](context))


def assing_execute(file_name):
    os.chmod(file_name, 0o755)


def is_bash(file_name):
    if file_name[-3:] == '.sh':
        assing_execute(file_name)


def exists(file_name):
    return os.path.isfile(file_name)
