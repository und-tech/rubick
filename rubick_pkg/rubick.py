import click
import os

from rubick_pkg.utils import file


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


cli = rubickCLI(help='Esta herramienta ayuda a crear proyetos en base a un scafold.')


@click.command(cls=rubickCLI)
@pass_context
def cli(ctx):
    pass
