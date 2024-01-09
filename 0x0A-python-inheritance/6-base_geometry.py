#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """
        Calculates the area of the BaseGeometry object.

        Returns:
            The area of the BaseGeometry object.

        Raises:
            NotImplementedError: This method should not be called directly.
            If it is called, an exception will be raised.
        """
        raise NotImplementedError("area() is not implemented")
