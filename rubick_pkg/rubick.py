import click
import os

from git import Repo
from os.path import expanduser
from rubick_pkg.utils import dir, file


config_folder = os.path.join(os.path.dirname(__file__), 'config.yaml')
command_folder = os.path.join(os.path.dirname(__file__), 'commands')


class Context(object):
    def __init__(self):
        self.config = file.read_yml(config_folder)


pass_context = click.make_pass_decorator(Context, ensure=True)


class rubickCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(command_folder):
            if filename.endswith('.py'):
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            ns = {}
            fn = os.path.join(command_folder, name + '.py')
            with open(fn) as f:
                code = compile(f.read(), fn, 'exec')
                eval(code, ns, ns)
            return ns['command']
        except Exception as e:
            return


cli = rubickCLI(help='Esta herramienta ayuda a crear proyectos en base a un scaffold.')


@click.command(cls=rubickCLI)
@pass_context
def cli(ctx):
    ctx.scaffolds_remote_repo = ctx.config['scaffolds']['url']
    ctx.scaffolds_local_repo = os.path.join(expanduser("~"), 'rubick-scaffolds')

    if not dir.exists(ctx.scaffolds_local_repo):
        Repo.clone_from(ctx.scaffolds_remote_repo, ctx.scaffolds_local_repo)
