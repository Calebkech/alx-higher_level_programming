#!/usr/bin/python3

"""Define a class Square."""

class Square:
    """Represent a Square here."""

    def __init__(self, size=0):
        """Initialize new square here.
        
        Args: 
            size (int): The size of new square.
        """
        self.__size = size

    @property
    def size(self):
        """get/set the current value of Square"""

        return(self.__size)
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value

    def area(self):
        """Return Square"""
        return(self.__size * self.__size)
    