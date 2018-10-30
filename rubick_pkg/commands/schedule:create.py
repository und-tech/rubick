
import click
import os

from rubick_pkg.context import pass_context
from rubick_pkg.utils import dir, file, try_execpt
from rubick_pkg.responses import CREATED_FILES, SUCCESSFUL_COMMAND, TITTLE_BAR, END_BAR


@click.command()
@click.option('--name', default='my_project', prompt='Ingresa el nombre de tu proyecto',
              help='Nombre del proyecto.')
@click.option('--product_name', default='undefined', prompt='Ingresa el nombre del producto',
              help='Nombre del producto.')
@click.option('--domain', default='undefined', prompt='Ingresa el nombre de dominio del producto',
              help='Nombre de dominio del producto.')
@click.option('--command_name', default='undefined', prompt='Ingresa el nombre del comando',
              help='Nombre del comando.')
@pass_context
@try_execpt.handler
def command(ctx, **kwargs):
    __create_project(**kwargs)
    ctx.logger.info(SUCCESSFUL_COMMAND)


def __create_project(**kwargs):
    scaffold = dir.get_scaffold_dir(paths=['schedule', 'create'])

    # set schedule package
    kwargs['package'] = 'schedules'

    click.echo(TITTLE_BAR % CREATED_FILES)
    for root, dirs, files in os.walk(scaffold):
        for file_name in files:
            # template content
            template_content = file.read(os.path.join(root, file_name))

            # paths for new project
            project_path = root.replace('+package+', kwargs['package'])\
                .replace(scaffold, os.path.join('.', kwargs['name']))\
                .replace(scaffold, os.path.join('.', kwargs['name']))

            full_file_name = os.path.join(project_path, file_name
                                          .replace('+command_name+.py', '%s.py' % kwargs['command_name'])
                                          .replace('+owner+', kwargs['product_name']))

            dir.create_file_path(full_file_name=full_file_name)
            file.create_rich_file(full_file_name=full_file_name, template=template_content, **kwargs)

            # created files
            click.echo(full_file_name)
    click.echo(END_BAR)
