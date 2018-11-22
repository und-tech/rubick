import click
import os
import json

from rubick_pkg.context import pass_context
from rubick_pkg.utils import try_execpt, file, dir
from rubick_pkg.responses import TITTLE_BAR, CREATED_FILES, END_BAR, SCAFFOLD_HAS_NOT_BASE
from rubick_pkg.constants import SCAFFOLD_FILE_NAME


@click.command()
@click.option('--scaffold_name', prompt='Enter the scaffold name', help='Scaffold name.')
@click.option('--name', default='my_project', prompt='Enter the project name', help='Project name.')
@pass_context
@try_execpt.handler
def command(ctx, scaffold_name, **kwargs):
    scaffold_dir = dir.get_scaffold_dir(paths=[scaffold_name])
    scaffold_data = file.read_yml(os.path.join(scaffold_dir, SCAFFOLD_FILE_NAME))
    project_path = os.path.join(ctx.pwd, kwargs['name'])
    prompts = __launch_prompts(scaffold_data)
    prompts.update(kwargs)

    if scaffold_data.get('scaffold', False):
        click.echo(TITTLE_BAR % CREATED_FILES)
        for root, dirs, files in os.walk(scaffold_dir):
            for file_name in files:
                # template content
                template_content = file.read(os.path.join(root, file_name))

                # paths for new project
                file_path = root.replace(scaffold_dir, project_path)
                full_file_name = __replace_names(search=scaffold_data, replace=prompts,
                                                 subject=os.path.join(file_path, file_name))

                dir.create_file_path(full_file_name=full_file_name)

                file.create(file_name=full_file_name, template_content=template_content, **prompts)

                # created files
                click.echo(full_file_name)

        # Save prompts data in project directory
        __save_prompts_data(scaffold_data, project_path, **prompts)

        # Remove .scaffold file from project
        __remove_scaffold_file(project_path)

        click.echo(END_BAR)
    else:
        raise Exception(SCAFFOLD_HAS_NOT_BASE)


def __launch_prompts(scaffold_data):
    inputs = dict()
    if scaffold_data.get('scaffold', {}).get('prompts', False):
        for prompt in scaffold_data['scaffold']['prompts']:
            inputs[prompt['name']] = click.prompt(prompt['description'], default=prompt['default'])
    return inputs


def __replace_names(search, replace, subject):
    new_subject = subject
    if search.get('scaffold', {}).get('replace_names', False):
        for replace_data in search['scaffold']['replace_names']:
            new_subject = new_subject.replace('%s' % replace_data['search'], '%s' % replace[replace_data['use_prompt']])
    return new_subject


def __save_prompts_data(scaffold_data, project_path, **prompts):
    if scaffold_data.get('scaffold', {}).get('save_prompts', False):
        prompts_file = os.path.join(project_path, scaffold_data['scaffold']['save_prompts'])
        file.create(file_name=prompts_file)
        file.append(prompts_file, json.dumps(prompts))


def __remove_scaffold_file(project_path):
    os.remove(os.path.join(project_path, SCAFFOLD_FILE_NAME))
