import os
import click

from os.path import expanduser
from rubick_pkg.utils import file, logger
from rubick_pkg.constants import CONFIG_FOLDER


class Context(object):
    def __init__(self):
        try:
            self.pwd = os.getcwd()
            self.config = file.read_yml(CONFIG_FOLDER)
            self.logger = logger.create('rubick_logger')
            self.scaffolds_remote = self.config['scaffolds']['url']
            self.scaffolds_local = os.path.join(expanduser("/tmp"), 'rubick-scaffolds')
        except Exception as e:
            raise e


pass_context = click.make_pass_decorator(Context, ensure=True)
