import click


@click.group(short_help="datagov CLI.")
def datagov():
    """datagov CLI.
    """
    pass


@datagov.command()
@click.argument("name", default="datagov")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [datagov]
