#!/usr/bin/python3
"""a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        # Check if size is an integer
        self.integer_validator("size", size)

        # Call the Rectangle constructor with the same arguments
        super().__init__(size, size)

        # Save the size of the square
        self.__size = size
