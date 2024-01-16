# Almost a Circle - Python Project

python3 -m unittest tests/test_models/test_base.py

Circle

This project focuses on object-oriented programming in Python, implementing three interconnected classes to represent rectangles and squares. The test suite, developed using the unittest module, thoroughly validates the functionality of each class.

Python Tools Used
Import
Exceptions
Private attributes
Getter/setter
Class/static methods
Inheritance
File I/O
args/kwargs
JSON and CSV serialization/deserialization
Unittesting
Tests :heavy_check_mark:
tests/test_models
test_base.py
test_rectangle.py
test_square.py
Classes :cl:
Base
Represents the base class for all other project classes. Includes:

Private class attribute __nb_objects = 0.
Public instance attribute id.
Class constructor def __init__(self, id=None):
If id is None, increments __nb_objects and assigns its value to the public instance attribute id.
Otherwise, sets the public instance attribute id to the provided id.
Static method def to_json_string(list_dictionaries): returns the JSON string serialization of a list of dictionaries.
Returns "[]" if list_dictionaries is None or empty.
Class method def save_to_file(cls, list_objs): writes the JSON serialization of a list of objects to a file.
Saves an empty list if list_objs is None.
File name: <cls name>.json (e.g., Rectangle.json).
Overwrites the file if it exists.
Static method def from_json_string(json_string): returns a list of objects deserialized from a JSON string.
Returns an empty list if json_string is None or empty.
Class method def create(cls, **dictionary): instantiates an object with provided attributes.
Class method def load_from_file(cls): returns a list of objects instantiated from a JSON file.
Returns an empty list if the file does not exist.
Class methods for CSV serialization/deserialization.
Static method def draw(list_rectangles, list_squares): draws Rectangle and Square instances in a GUI window using the turtle module.
Rectangle
Represents a rectangle. Inherits from Base with:

Private instance attributes __width, __height, __x, and __y.
Class constructor def __init__(self, width, height, x=0, y=0, id=None):
Public methods for area, display, update, and to_dictionary.
Square
Represents a square. Inherits from Rectangle with:

Class constructor def __init__(self, size, x=0, y=0, id=None):
Public methods for update and to_dictionary.