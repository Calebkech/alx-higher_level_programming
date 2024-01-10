#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout.

    Args:
        filename (str, optional): The path to the file. Defaults to "".

    Returns:
        None

    Raises:
        FileNotFoundError: If the file does not exist.
        IsADirectoryError: If the path points to a directory.
        OSError: If there is an error opening or reading the file.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
