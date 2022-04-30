"""Console script for deluge_cmd."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("deluge_cmd")
    click.echo("=" * len("deluge_cmd"))
    click.echo("cli tools to manage deluge sd card contents")


if __name__ == "__main__":
    main()  # pragma: no cover
