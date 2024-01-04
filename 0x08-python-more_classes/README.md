# 0x08. Python - More Classes and Objects

## Overview

In this project, I delved deeper into object-oriented programming in Python. The focus was on understanding class methods, static methods, class vs instance attributes, and the utilization of special methods such as `__str__` and `__repr__`.

## Directory Structure

- [tests](./tests): Folder containing test files provided by ALX.

## Tasks

### 0. Simple Rectangle

- [0-rectangle.py](./0-rectangle.py): Defines an empty Python class representing a rectangle.

### 1. Real Definition of a Rectangle

- [1-rectangle.py](./1-rectangle.py): Enhances the `Rectangle` class with private attributes `width` and `height`, along with their respective getters and setters. The class is instantiated with optional `width` and `height` parameters, raising errors for invalid input.

### 2. Area and Perimeter

- [2-rectangle.py](./2-rectangle.py): Adds public instance methods `area` and `perimeter` to the `Rectangle` class. The `area` method calculates the area, and the `perimeter` method calculates the perimeter (with additional conditions).

### 3. String Representation

- [3-rectangle.py](./3-rectangle.py): Implements the `__str__` special method to provide a human-readable string representation of the `Rectangle` class.

### 4. Eval is Magic

- [4-rectangle.py](./4-rectangle.py): Enhances the `Rectangle` class with the `__repr__` special method, returning a string representation of the object.

### 5. Detect Instance Deletion

- [5-rectangle.py](./5-rectangle.py): Introduces the `__del__` special method, which prints a message when an instance of the `Rectangle` class is deleted.

### 6. How Many Instances

- [6-rectangle.py](./6-rectangle.py): Adds a public class attribute `number_of_instances` to the `Rectangle` class, tracking the number of instances created and deleted.

### 7. Change Representation

- [7-rectangle.py](./7-rectangle.py): Introduces a public class attribute `class_symbol` to the `Rectangle` class, allowing customization of the symbol used in the string representation.

### 8. Compare Rectangles

- [8-rectangle.py](./8-rectan
gle.py): Implements a static method `bigger_or_equal` in the `Rectangle` class to compare two rectangles based on their areas.

### 9. A Square is a Rectangle

- [9-rectangle.py](./9-rectangle.py): Introduces a class method `square` to create a new `Rectangle` instance with equal width and height.

### 10. N Queens

- [101-nqueens.py](./101-nqueens.py): Solves the N queens puzzle, finding all possible solutions for placing N non-attacking queens on an NxN chessboard. The program takes N as a command-line argument.

## Conclusion

This project provided a comprehensive exploration of advanced concepts in classes and objects in Python, emphasizing practical implementations and problem-solving skills.
