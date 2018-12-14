import os
import yaml
import json
import re

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


def assign_execute(file_name):
    os.chmod(file_name, 0o755)


def is_bash(file_name):
    if file_name[-3:] == '.sh':
        assign_execute(file_name)


def exists(file_name):
    return os.path.isfile(file_name)


def create_rich_file(full_file_name, template, **kwargs):
    create(full_file_name, template, **kwargs)
    is_bash(full_file_name)
    is_executable(full_file_name)


def is_executable(full_file_name):
    if re.match('^[\w/]+(\/bin\/)[\w]*$', full_file_name):
        assign_execute(full_file_name)
