
import click
import os

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
@click.option('--package', default='context', prompt='Ingresa el nombre del paquete principal para tu app',
              help='Nombre del paquete.')
@pass_context
def command(ctx, **kwargs):
    try:
        scaffold_project_dir = os.path.join(ctx.scaffolds_local_repo, 'schedule', 'create')

        if dir.exists(scaffold_project_dir):
            print("== Archivos creados ==")
            for root, dirs, files in os.walk(scaffold_project_dir):
                for file_name in files:
                    ## template content ##
                    template_content = file.read(os.path.join(root, file_name))

                    ## paths for new project ##
                    new_project_path = root.replace('+package+', kwargs['package'])\
                                           .replace(scaffold_project_dir, os.path.join('.', kwargs['name'])) \
                                           .replace(scaffold_project_dir, os.path.join('.', kwargs['name']))

                    new_file_path = os.path.join(new_project_path, file_name
                                                 .replace('+command_name+.py', '%s.py' % kwargs['command_name'])
                                                 .replace('+owner+_schedules', '%s_schedules' % kwargs['product_name']))

                    new_dir_path = os.path.dirname(new_file_path)

                    ## create project ##
                    dir.create(new_dir_path)
                    file.create(new_file_path, template_content, **kwargs)

                    ## created files ##
                    print(new_file_path)
        else:
            print('No se encontro el directorio base para la creación del proyecto schedule')
    except Exception as e:
        print("== Ocrrio un problema durante la creación ==")
        print("="*10)
        print(e)
