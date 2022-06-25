"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """The Antidote Book."""


if __name__ == "__main__":
    main(prog_name="antidote-book")  # pragma: no cover
