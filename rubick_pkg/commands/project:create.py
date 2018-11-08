import click
import os

from rubick_pkg.context import pass_context
from rubick_pkg.utils import try_execpt, file, dir
from rubick_pkg.responses import TITTLE_BAR, CREATED_FILES, END_BAR


@click.command()
@click.option('--scaffold_name', prompt='Ingrese el nombre del scaffold')
@click.option('--product_name', type=click.Choice(['urbania', 'neo', 'aptitus', 'pagoefectivo']),
              prompt='Ingresa el nombre del producto [urbania, neo, aptitus, pagoefectivo]',
              help='Nombre del producto.')
@click.option('--name', default='my_project', prompt='Ingresa el nombre de tu proyecto',
              help='Nombre del proyecto.')
@pass_context
@try_execpt.handler
def command(ctx, scaffold_name, **kwargs):
    scaffold_dir = dir.get_scaffold_dir(paths=[scaffold_name])
    scaffold_data = file.read_yml(os.path.join(scaffold_dir, '.scaffold'))
    prompts = __launch_prompts(scaffold_data)
    prompts.update(kwargs)

    click.echo(TITTLE_BAR % CREATED_FILES)
    for root, dirs, files in os.walk(scaffold_dir):
        for file_name in files:
            # template content
            template_content = file.read(os.path.join(root, file_name))

            # paths for new project
            project_path = root.replace(scaffold_dir, os.path.join('.', prompts['name']))
            full_file_name = __replace_names(search=scaffold_data, replace=prompts, subject=os.path.join(project_path,
                                                                                                         file_name))

            dir.create_file_path(full_file_name=full_file_name)

            file.create(file_name=full_file_name, template_content=template_content, **prompts)

            # created files
            click.echo(full_file_name)
    click.echo(END_BAR)


def __launch_prompts(scaffold_data):
    inputs = dict()
    for prompt in scaffold_data['base']['prompts']:
        inputs[prompt['name']] = click.prompt(prompt['description'], default=prompt['default'])
    return inputs


def __replace_names(search, replace, subject):
    for replace_data in search['base']['replace_names']:
        return subject.replace('%s' % replace_data['search'], '%s' % replace[replace_data['use_prompt']])
