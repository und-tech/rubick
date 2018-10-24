
import click
import os
import traceback

from rubick_pkg.rubick import pass_context
from rubick_pkg.utils import dir, file


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
def command(ctx, **kwargs):
    try:
        scaffold_project_dir = os.path.join(ctx.scaffolds_local_repo, 'schedule', 'create')

        # Check scaffold template
        if not dir.exists(scaffold_project_dir):
            raise Exception('No se encontro el directorio base para el schedule, utiliza rubick scaffolds:update')

        # set schedule package
        kwargs['package'] = 'schedules'

        ctx.logger.info("== Archivos creados ==")
        for root, dirs, files in os.walk(scaffold_project_dir):
            for file_name in files:
                # template content
                template_content = file.read(os.path.join(root, file_name))

                # paths for new project
                new_project_path = root.replace('+package+', kwargs['package'])\
                                       .replace(scaffold_project_dir, os.path.join('.', kwargs['name'])) \
                                       .replace(scaffold_project_dir, os.path.join('.', kwargs['name']))

                new_file_path = os.path.join(new_project_path, file_name
                                             .replace('+command_name+.py', '%s.py' % kwargs['command_name'])
                                             .replace('+owner+', kwargs['product_name']))

                new_dir_path = os.path.dirname(new_file_path)

                # create project
                if not dir.create(new_dir_path):
                    raise Exception('No se pudo crear el directorio: %s' % new_dir_path)

                file.create(new_file_path, template_content, **kwargs)

                executable_file = 'bin/%s' % kwargs['product_name']
                if new_file_path.endswith(executable_file):
                    file.assing_execute(new_file_path)

                # created files
                print(new_file_path)
    except Exception as e:
        ctx.logger.error(e)
        if ctx.verbose:
            ctx.logger.error(traceback.format_exc())
