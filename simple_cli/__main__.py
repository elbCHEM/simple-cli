import click
from simple_cli.hello import hello
from simple_cli.get_cwd import get_cwd as _get_cwd


@click.group
def main() -> None: ...


main.command(hello)


@main.command()
@click.option("--absolute", type=click.BOOL, is_flag=True, default=False, help="Print the absolute path.")
def get_cwd(absolute: bool) -> None:
    _get_cwd(absolute)


if __name__ == '__main__':
    main()
