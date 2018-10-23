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
@click.option('--container_port', default='8080', prompt='Ingresa el puerto para la aplicación',
              help='Puerto para la aplicación. Es utilizado por Docker y por TaskDefinition')
@click.option('--slack_web_hook', default='undefined', prompt='Ingresa el webhook para las notificaciones de slack',
              help='Webhook para notificaciones de despliegue, se utiliza en la ejecución de Job de Jenkins.')
@click.option('--https_listener_dev', default='undefined', prompt='Ingresa el arn del listener para el ambiente de DEV',
              help='ARN asociado al listener de DEV, se utiliza dentro de cloudformation.')
@click.option('--https_listener_pre', default='undefined', prompt='Ingresa el arn del listener para el ambiente de PRE',
              help='ARN asociado al listener de PRE, se utiliza dentro de cloudformation.')
@click.option('--https_listener_prod', default='undefined', prompt='Ingresa el arn del listener para el ambiente de PROD',
              help='ARN asociado al listener de PROD, se utiliza dentro de cloudformation.')
@click.option('--vpc_dev', default='undefined', prompt='Ingresa el arn de la vpc para el ambiente de DEV',
              help='ARN asociado a la VPC de DEV, se utiliza dentro de cloudformation.')
@click.option('--vpc_pre', default='undefined', prompt='Ingresa el arn de la vpc para el ambiente de PRE',
              help='ARN asociado a la VPC de PRE, se utiliza dentro de cloudformation.')
@click.option('--vpc_prod', default='undefined', prompt='Ingresa el arn de la vpc para el ambiente de PROD',
              help='ARN asociado a la VPC de PROD, se utiliza dentro de cloudformation.')
@click.option('--https_priority', default='undefined', prompt='Ingresa la prioridad del listener https',
              help='Prioridad de listener HTTPS en el ALB, este número cambia de acuerdo al ambiente.')
@pass_context
def command(ctx, **kwargs):
    try:
        scaffold_project_dir = os.path.join(ctx.scaffolds_local_repo, 'rest')

        # Check scaffold template
        if not dir.exists(scaffold_project_dir):
            raise Exception('No se encontro el directorio base para el api rest, utiliza rubick scaffolds:update')

        ctx.logger.info("== Archivos creados ==")
        for root, dirs, files in os.walk(scaffold_project_dir):
            for file_name in files:
                    # template content
                    template_content = file.read(os.path.join(root, file_name))

                    # paths for new project
                    new_project_path = root.replace('+package+', kwargs['package']).replace(scaffold_project_dir, os.path.join('.', kwargs['name']))
                    new_file_path = os.path.join(new_project_path, file_name)
                    new_dir_path = os.path.dirname(new_file_path)

                    # create project
                    if not dir.create(new_dir_path):
                        raise Exception('No se pudo crear el directorio: %s' % new_dir_path)

                    file.create(new_file_path, template_content, **kwargs)

                    # created files
                    print(new_file_path)
    except Exception as e:
        ctx.logger.error(e)
