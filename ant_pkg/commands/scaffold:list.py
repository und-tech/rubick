import click
import os

from terminaltables import AsciiTable
from ant_pkg.context import pass_context
from ant_pkg.utils import try_execpt, file


@click.command()
@pass_context
@try_execpt.handler
def command(ctx):
    dirs = os.listdir(ctx.scaffolds_local)
    table_data = [
        ['Scaffold Name', 'Description', 'Author']
    ]
    for dir in dirs:
        if dir[0] is not '.':
            try:
                scaffold = file.read_yml(os.path.join(ctx.scaffolds_local, dir, '.scaffold'))
                table_data.append([scaffold['scaffold']['name'],
                                   scaffold['scaffold']['description'],
                                   scaffold['scaffold']['author']
                                   ]
                                  )
            except Exception as e:
                pass
    table = AsciiTable(table_data)
    click.echo(table.table)
    click.echo()
    click.echo('*****')
    click.echo('Note:')
    click.echo('*****')
    click.echo('Use "scaffold:update" if you dont see your template.')
