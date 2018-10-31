import click
import importlib

from rubick_pkg.context import pass_context
from rubick_pkg.utils import try_execpt


@click.command()
@click.option('--language', type=click.Choice(['python', 'netCore', 'nodeJS']),
              prompt='Lenguaje de programación [python, netCore, nodeJS]')
@click.option('--product_name', type=click.Choice(['urbania', 'neo', 'aptitus', 'pagoefectivo']),
              prompt='Ingresa el nombre del producto [urbania, neo, aptitus, pagoefectivo]',
              help='Nombre del producto.')
@click.option('--name', default='my_project', prompt='Ingresa el nombre de tu proyecto',
              help='Nombre del proyecto.')
@pass_context
@try_execpt.handler
def command(ctx, language, product_name, name):
    module = importlib.import_module('rubick_pkg.commands.api.%s.create' % language)
    sub_command = getattr(module, '__create_project')
    click.get_current_context().forward(sub_command)
