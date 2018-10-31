import click
import os

from rubick_pkg.context import pass_context
from rubick_pkg.utils import dir, file
from rubick_pkg.responses import CREATED_FILES, TITTLE_BAR, END_BAR


@click.command()
@pass_context
def __create_project(ctx, **kwargs):
    kwargs.update(__launch_inputs())

    scaffold = dir.get_scaffold_dir(paths=['rest'])
    click.echo(TITTLE_BAR % CREATED_FILES)
    for root, dirs, files in os.walk(scaffold):
        for file_name in files:
            # template content
            template_content = file.read(os.path.join(root, file_name))

            # paths for new project
            project_path = root.replace('+package+', kwargs['package']).replace(scaffold,
                                                                                os.path.join('.', kwargs['name']))
            full_file_name = os.path.join(project_path, file_name)
            dir.create_file_path(full_file_name=full_file_name)

            file.create(file_name=full_file_name, template_content=template_content, **kwargs)

            # created files
            click.echo(full_file_name)
    click.echo(END_BAR)


def __launch_inputs():
    inputs = dict()
    inputs['package'] = click.prompt('Ingresa el nombre del paquete principal para tu app', default='context')
    inputs['api_version'] = click.prompt('Ingresa la versión de tu api rest', default='v1')
    inputs['container_port'] = click.prompt('Ingresa el puerto para la aplicación', default='8080')
    inputs['slack_web_hook'] = click.prompt('Ingresa el webhook para las notificaciones de slack', default='undefined')
    inputs['https_listener_dev'] = click.prompt('Ingresa el arn del listener para el ambiente de DEV',
                                                default='undefined')
    inputs['https_listener_pre'] = click.prompt('Ingresa el arn del listener para el ambiente de PRE',
                                                default='undefined')
    inputs['https_listener_prod'] = click.prompt('Ingresa el arn del listener para el ambiente de PROD',
                                                 default='undefined')
    inputs['vpc_dev'] = click.prompt('Ingresa el arn de la vpc para el ambiente de DEV', default='undefined')
    inputs['vpc_pre'] = click.prompt('Ingresa el arn de la vpc para el ambiente de PRE', default='undefined')
    inputs['vpc_prod'] = click.prompt('Ingresa el arn de la vpc para el ambiente de PROD', default='undefined')
    inputs['https_priority'] = click.prompt('Ingresa la prioridad del listener https', default='undefined')
    return inputs
