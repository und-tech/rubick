import click
import os
import traceback

from rubick_pkg.rubick import pass_context
from rubick_pkg.utils import dir, file


@click.command()
@click.option('--command_name', default='undefined', prompt='Ingresa el nombre del comando',
              help='Nombre del comando.')
@pass_context
def command(ctx, command_name):
    try:
        # Scaffold routes
        scaffold_base_path = os.path.join(ctx.scaffolds_local_repo, 'schedule', 'create')
        scaffold_command_dir = os.path.join(scaffold_base_path, 'schedules', 'commands')
        scaffold_cf_dir = os.path.join(scaffold_base_path, 'cloudformation', 'stacks', 'schedules.yml')

        # read origin project data
        rubick_data = file.read_json('rubick.json')
        rubick_data['variables']['command_name'] = command_name

        # current project paths
        project_base_path = os.getcwd()
        new_command_path = os.path.join(project_base_path, 'schedules', 'commands')
        cf_schedules_file = os.path.join(project_base_path, 'cloudformation', 'stacks', 'schedules.yml')

        for root, dirs, files in os.walk(scaffold_command_dir):
            for file_name in files:
                # template content
                command_template_content = file.read(os.path.join(root, file_name))

                file_path = os.path.join(new_command_path, file_name
                                         .replace('+command_name+.py', '%s.py' % command_name))
                if not file_path.endswith('__.py'):
                    file.create(file_path, command_template_content, **rubick_data['variables'])

        cf_schedule_content = file.get_template_block(scaffold_cf_dir, 'schedule_task', **rubick_data['variables'])
        file.append(cf_schedules_file, cf_schedule_content)

        ctx.logger.info("Se adiciono el comando de manera correcta")
    except Exception as e:
        ctx.logger.error(e)
        if ctx.verbose:
            ctx.logger.error(traceback.format_exc())
