import sys
from simple_cli.hello import hello
from simple_cli.get_cwd import get_cwd


def main() -> None:
    if 'hello' in sys.argv:
        hello()
        return
    if 'get-cwd' in sys.argv:
        get_cwd('--absolute' in sys.argv)
        return

    raise Exception('Could not find any command')


if __name__ == '__main__':
    main()
