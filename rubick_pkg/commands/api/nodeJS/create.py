import click

from rubick_pkg.context import pass_context


@click.command()
@pass_context
def __create_project(ctx, **kwargs):
    click.echo("nodeJS API")
    click.echo("Context")
    print(ctx)
    click.echo("Kwargs")
    print(kwargs)
