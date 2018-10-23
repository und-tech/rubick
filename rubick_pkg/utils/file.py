import os
import yaml
from jinja2 import Template


def read(file_path):
    try:
        return open(file_path, 'r').read()
    except Exception:
        return False


def read_yml(file_path):
    return yaml.load(read(file_path))


def create(file_name, template_content=None, **kwargs):
    f = open(file_name, "w+")
    if template_content is not None:
        template = Template(template_content)
        content = template.render(**kwargs)
        f.write(content)
    f.close()
    is_bash(file_name)


def assing_execute(file_name):
    os.chmod(file_name, 0o755)


def is_bash(file_name):
    if file_name[-3:] == '.sh':
        assing_execute(file_name)
