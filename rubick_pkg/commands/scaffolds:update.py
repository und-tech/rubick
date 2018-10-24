import click
import shutil
import traceback

from rubick_pkg.rubick import pass_context
from git import Repo


@click.command()
@pass_context
def command(ctx):
    try:
        shutil.rmtree(ctx.scaffolds_local_repo)
        Repo.clone_from(ctx.scaffolds_remote_repo, ctx.scaffolds_local_repo)
        ctx.logger.info("Se actualizo de manera correcta la versión de scaffolds.")
    except Exception as e:
        ctx.logger.error(e)
        if ctx.verbose:
            ctx.logger.error(traceback.format_exc())