import os
import pathlib


def get_cwd(absolute: bool = False) -> pathlib.Path:
    cwd = pathlib.Path(os.getcwd())

    if absolute:
        as_string = str(cwd.absolute())
    else:
        as_string = str(cwd)

    print(f"Current working directory is {as_string}")
    return cwd


if __name__ == '__main__':
    get_cwd(absolute=True)
