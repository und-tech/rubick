
import click
import os

from rubick_pkg.rubick import pass_context
from rubick_pkg.utils import dir, file, try_execpt
from rubick_pkg import SCAFFOLD_NOT_FOUND, CREATED_FILES, DIRECTORY_NOT_CREATED, SUCCESSFUL_COMMAND, TITTLE_BAR, END_BAR


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
    __create_project(ctx, **kwargs)
    ctx.logger.info(SUCCESSFUL_COMMAND)


def __create_file_path(full_file_name):
    path = os.path.dirname(full_file_name)
    # create project
    if not dir.create(path):
        raise Exception(DIRECTORY_NOT_CREATED % path)


def __create_file(full_file_name, template, **kwargs):
    file.create(full_file_name, template, **kwargs)
    executable_file = 'bin/%s' % kwargs['product_name']
    if full_file_name.endswith(executable_file):
        file.assing_execute(full_file_name)


def __create_project(ctx, **kwargs):
    scaffold = __get_scaffold_dir(ctx)

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

            __create_file_path(full_file_name=full_file_name)
            __create_file(full_file_name=full_file_name, template=template_content, **kwargs)

            # created files
            click.echo(full_file_name)
    click.echo(END_BAR)


def __get_scaffold_dir(ctx):
    scaffold_project_dir = os.path.join(ctx.scaffolds_local, 'schedule', 'create')
    if not dir.exists(scaffold_project_dir):
        raise Exception(SCAFFOLD_NOT_FOUND)
    return scaffold_project_dir
