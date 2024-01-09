#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Overrides the default == operator to invert the result.

        Args:
            value (int): The value to compare to.

        Returns:
            bool: Whether or not the two MyInt objects are equal.

        """
        return self.real != value

    def __ne__(self, value):
        """Overrides the default != operator to invert the result.

        Args:
            value (int): The value to compare to.

        Returns:
            bool: Whether or not the two MyInt objects are equal.

        """
        return self.real == value
