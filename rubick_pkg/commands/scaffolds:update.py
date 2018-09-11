import click
import shutil

from rubick_pkg.rubick import pass_context
from rubick_pkg.utils import dir
from git import Repo


@click.command()
@pass_context
def command(ctx):
    try:
        if dir.exists(ctx.scaffolds_local_repo):
            shutil.rmtree(ctx.scaffolds_local_repo)
        Repo.clone_from(ctx.scaffolds_remote_repo, ctx.scaffolds_local_repo)
        print("== Se actualizo los scaffolds con éxito ==")
    except Exception as e:
        print("== Ocrrio un problema durante la actualización ==")
        print("="*10)
        print(e)
