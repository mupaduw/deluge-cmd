"""Console script for deluge_cmd."""

import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("deluge_cmd:cli")
    click.echo("=" * len("deluge_cmd:cli"))
    click.echo("cli does nothing - use deluge_dls instead")


if __name__ == "__main__":
    main()  # pragma: no cover
