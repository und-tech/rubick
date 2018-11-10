import click
import os

from rubick_pkg.context import pass_context
from rubick_pkg.utils import try_execpt, file


@click.command()
@pass_context
@try_execpt.handler
def command(ctx):
    dirs = os.listdir(ctx.scaffolds_local)
    for dir in dirs:
        if dir[0] is not '.':
            try:
                scaffold = file.read_yml(os.path.join(ctx.scaffolds_local, dir, '.scaffold'))
                click.echo('---')
                click.echo('ScaffoldName: %s' % scaffold['base']['scaffold_name'])
                click.echo('Description: %s' % scaffold['base']['description'])
            except Exception as e:
                pass
    click.echo()
    click.echo('*****')
    click.echo('Note:')
    click.echo('*****')
    click.echo('Use "scaffolds:update" if you dont see your template.')
