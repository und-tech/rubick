import click
import os

from rubick_pkg.rubick import pass_context
from rubick_pkg.utils import dir, file


@click.command()
@click.option('--name', default='my_project', prompt='Ingresa el nombre de tu proyecto',
              help='Nombre del proyecto.')
@click.option('--product_name', default='undefined', prompt='Ingresa el nombre del producto',
              help='Nombre del producto.')
@click.option('--package', default='context', prompt='Ingresa el nombre del paquete principal para tu app',
              help='Nombre del paquete.')
@click.option('--api_version', default='v1', prompt='Ingresa la versión de tu api rest',
              help='Versión de tu api rest.')
@pass_context
def command(ctx, **kwargs):
    scaffold_project_dir = os.path.join(ctx.scaffolds_local_repo, 'rest')

    if dir.exists(scaffold_project_dir):
        for root, dirs, files in os.walk(scaffold_project_dir):
            for file_name in files:
                    ## template content ##
                    template_content = file.read(os.path.join(root, file_name))

                    ## paths for new project ##
                    new_project_path = root.replace('+package+', kwargs['package']).replace(scaffold_project_dir, os.path.join('.', kwargs['name']))
                    new_file_path = os.path.join(new_project_path, file_name)
                    new_dir_path = os.path.dirname(new_file_path)

                    ## create project ##
                    dir.create(new_dir_path)
                    file.create(new_file_path, template_content, **kwargs)

                    ## created files ##
                    print("== Archivos creados ==")
                    print(new_file_path)
    else:
        print('No se encontro el directorio base para el api rest')
