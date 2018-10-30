import click
import os

from rubick_pkg.context import pass_context
from rubick_pkg.utils import file, dir, try_execpt
from rubick_pkg.responses import SUCCESSFUL_COMMAND, NOT_RUBICK_FILE


@click.command()
@click.option('--command_name', default='undefined', prompt='Ingresa el nombre del comando',
              help='Nombre del comando.')
@pass_context
@try_execpt.handler
def command(ctx, command_name):
    scaffold_command, scaffold_cloud_formation = __get_scaffold_paths()

    # generate variables for templates
    template_variables = __generate_template_variables(ctx, command_name)

    # get project command path and cloud formation file
    commands_path, cloud_formation_file = __get_project_paths(ctx)

    # adding the new command
    __add_command(scaffold=scaffold_command, path=commands_path, **template_variables)

    # append data in cloud formation
    __append_cloud_formation(scaffold=scaffold_cloud_formation, file_path=cloud_formation_file, **template_variables)

    ctx.logger.info(SUCCESSFUL_COMMAND)


def __add_command(scaffold, path, **tmp_data):
    walked = dir.walk(scaffold)
    command_tmp = file.read(os.path.join(walked[0]['root'], walked[0]['files'][0]))
    file_path = os.path.join(path, walked[0]['files'][0].replace('+command_name+.py',
                                                                 '%s.py' % tmp_data['command_name']))
    # create the command file
    file.create(file_name=file_path, template_content=command_tmp, **tmp_data)


def __append_cloud_formation(scaffold, file_path, **tmp_data):
    template = file.get_template_block(file_path=scaffold, block='schedule_task', **tmp_data)

    # append data in cloud formation
    file.append(file_path=file_path, content=template)


def __generate_template_variables(ctx, command_name):
    if ctx.rubick_data is None:
        raise Exception(NOT_RUBICK_FILE)
    ctx.rubick_data['variables']['command_name'] = command_name
    return ctx.rubick_data['variables']


def __get_scaffold_paths():
    base_path = ['schedule', 'create']
    scaffold_command = dir.get_scaffold_dir(paths=base_path + ['schedules', 'commands'])
    scaffold_cloud_formation = dir.get_scaffold_dir(paths=base_path + ['cloudformation', 'stacks', 'schedules.yml'])
    return scaffold_command, scaffold_cloud_formation


def __get_project_paths(ctx):
    project_command_path = os.path.join(ctx.pwd, 'schedules', 'commands')
    project_cloud_formation_file = os.path.join(ctx.pwd, 'cloudformation', 'stacks', 'schedules.yml')
    return project_command_path, project_cloud_formation_file
