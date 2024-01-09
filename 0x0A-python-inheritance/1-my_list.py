#!/usr/bin/python3
"""
contains the MyList class
"""

class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """
        initializes the object
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the sorted list.

        Parameters:
            self (MyList): The instance of the MyList class.

        Returns:
            None

        """
        print(sorted(self))
