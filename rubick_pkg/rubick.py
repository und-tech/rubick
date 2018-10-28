import click
import os

from git import Repo
from os.path import expanduser
from rubick_pkg.utils import dir, file, logger, try_execpt
from rubick_pkg import HELP_DESCRIPTION, RUBICK_FILE_NAME


config_folder = os.path.join(os.path.dirname(__file__), 'config.yaml')
command_folder = os.path.join(os.path.dirname(__file__), 'commands')


class Context(object):
    def __init__(self):
        try:
            self.pwd = os.getcwd()
            self.config = file.read_yml(config_folder)
            self.logger = logger.create('rubick_logger')
            self.scaffolds_remote = self.config['scaffolds']['url']
            self.scaffolds_local = os.path.join(expanduser("~"), 'rubick-scaffolds')
            self.rubick_data = file.read_json(RUBICK_FILE_NAME) if file.exists(RUBICK_FILE_NAME) else None
        except Exception as e:
            raise e


pass_context = click.make_pass_decorator(Context, ensure=True)


class RubickCLI(click.MultiCommand):
    def list_commands(self, ctx):
        try:
            rv = []
            for filename in os.listdir(command_folder):
                if filename.endswith('.py'):
                    rv.append(filename[:-3])
            rv.sort()
            return rv
        except Exception as e:
            log = logger.create('list_command_logger')
            log.error(e)

    def get_command(self, ctx, name):
        try:
            ns = {}
            fn = os.path.join(command_folder, name + '.py')
            with open(fn) as f:
                code = compile(f.read(), fn, 'exec')
                eval(code, ns, ns)
            return ns['command']
        except KeyError:
            pass
        except Exception as e:
            log = logger.create('get_command_logger')
            log.error(e)


cli = RubickCLI(help=HELP_DESCRIPTION)


@click.command(cls=RubickCLI)
@click.option('-v', '--verbose', is_flag=True, help='Activa el traceback del código.')
@pass_context
@try_execpt.handler
def cli(ctx, verbose):
    ctx.verbose = verbose
    if not dir.exists(ctx.scaffolds_local):
        Repo.clone_from(ctx.scaffolds_remote, ctx.scaffolds_local)
