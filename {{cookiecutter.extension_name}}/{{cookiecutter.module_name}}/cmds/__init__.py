import click

from aprsd.cli_helper import AliasedGroup
from aprsd.main import cli


@cli.group(cls=AliasedGroup, aliases=['{{cookiecutter.extension_group_name}}'], help="{{cookiecutter.short_description}}")
@click.pass_context
def {{cookiecutter.extension_group_name}}(ctx):
    pass
