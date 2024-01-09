#!/usr/bin/python3
"""Defines an object attribute lookup function."""

def lookup(obj):
    """Return a list of an object's available attributes.

    Args:
        obj (object): The object to retrieve attributes from.

    Returns:
        list: A list of the object's attributes.
    """
    return (dir(obj))
