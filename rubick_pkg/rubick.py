import click
import os

from git import Repo
from rubick_pkg.context import pass_context
from rubick_pkg.utils import dir, logger, try_execpt
from rubick_pkg.responses import HELP_DESCRIPTION
from rubick_pkg.constants import COMMAND_FOLDER


class RubickCLI(click.MultiCommand):
    def list_commands(self, ctx):
        try:
            rv = []
            for filename in os.listdir(COMMAND_FOLDER):
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
            fn = os.path.join(COMMAND_FOLDER, name + '.py')
            with open(fn) as f:
                code = compile(f.read(), fn, 'exec')
                eval(code, ns, ns)
            return ns['command']
        except (KeyError, FileNotFoundError):
            pass
        except Exception as e:
            log = logger.create('get_command_logger')
            log.error(e)


cli = RubickCLI(help=HELP_DESCRIPTION)


@click.command(cls=RubickCLI)
@click.option('-v', '--verbose', is_flag=True, help='Activa el traceback del código.')
@click.option('--scaffolds', default=False, type=click.Path(),
              help='Coloca la ruta absoluta de tus scaffolds personalizados.')
@pass_context
@try_execpt.handler
def cli(ctx, verbose, scaffolds):
    ctx.verbose = verbose

    if scaffolds:
        ctx.scaffolds_local = scaffolds

    if not dir.exists(ctx.scaffolds_local):
        Repo.clone_from(ctx.scaffolds_remote, ctx.scaffolds_local)
