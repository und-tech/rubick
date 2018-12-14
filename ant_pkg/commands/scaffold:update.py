import click
import shutil
import os
import time

from ant_pkg.ant import pass_context
from ant_pkg.utils import try_execpt
from ant_pkg.responses import SUCCESSFUL_COMMAND
from git import Repo


@click.command()
@pass_context
@try_execpt.handler
def command(ctx):
    shutil.rmtree(ctx.scaffolds_local)
    while os.path.isdir(ctx.scaffolds_local):
        time.sleep(0.1)
    Repo.clone_from(ctx.scaffolds_remote, ctx.scaffolds_local)
    ctx.logger.info(SUCCESSFUL_COMMAND)
