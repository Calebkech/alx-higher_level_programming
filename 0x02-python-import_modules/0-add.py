#!/usr/bin/python3
if __name__ == "__main__":
    # Import the add function from add_0.py
    from add_0 import add
    a = 1
    b = 2
    # Print the result using string formatting
    c = add(a,b)
    print("{} + {} = {}".format(a, b, add(a,b)))
