#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represent a Square here."""

    def __init__(self, size=0):
        """Initialize new square here.
        
        Args: 
            size (int): The size of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size

    def area(self):
        """Return Square"""
        return(self.__size * self.__size)
    