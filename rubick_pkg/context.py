import os
import click

from os.path import expanduser
from rubick_pkg.utils import file, logger
from rubick_pkg.constants import RUBICK_FILE_NAME, CONFIG_FOLDER


class Context(object):
    def __init__(self):
        try:
            self.pwd = os.getcwd()
            self.config = file.read_yml(CONFIG_FOLDER)
            self.logger = logger.create('rubick_logger')
            self.scaffolds_remote = self.config['scaffolds']['url']
            self.scaffolds_local = os.path.join(expanduser("/tmp"), 'rubick-scaffolds')
            self.rubick_data = file.read_json(RUBICK_FILE_NAME) if file.exists(RUBICK_FILE_NAME) else None
        except Exception as e:
            raise e


pass_context = click.make_pass_decorator(Context, ensure=True)
