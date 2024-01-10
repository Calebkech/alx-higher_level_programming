# 0x0B. Python - Input/Output

## Project Overview

- **Language:** Python
- **Author:** Guillaume
- **Weight:** 1
- **Ongoing second chance project:** Started Jan 9, 2024, 6:00 AM, must end by Jan 11, 2024, 6:00 AM
- **Auto review:** An auto review will be launched at the deadline

## Resources

- Various resources on file handling, JSON, and Python programming.

## Learning Objectives

- Cover various aspects of Python input/output operations, file handling, and JSON serialization/deserialization.

## Copyright - Plagiarism

- Strictly forbid plagiarism.
- No publishing of project content.
- Any form of plagiarism results in removal from the program.

## Requirements

### Python Scripts

- Use specified editors (vi, vim, emacs).
- Interpret on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- Follow specified conventions.
- Use pycodestyle (version 2.8.*).
- Files must be executable.
- Length of files will be tested using `wc`.

### Python Test Cases

- Test files in a `tests` folder.
- Test files are text files (`.txt`).
- Execute tests using `python3 -m doctest ./tests/*`.
- Include documentation for modules, classes, and functions.
- Documentation must be descriptive sentences.

## Tasks

### 0. Read file

- Function `read_file` reads a text file (UTF8) and prints it to stdout.
- Use the `with` statement.
- No need to manage file permissions or exceptions.
- Do not import any module.

### 1. Write to a file

- Function `write_file` writes a string to a text file (UTF8) and returns the number of characters written.
- Use the `with` statement.
- Do not manage file permission exceptions.
- Create the file if it doesn’t exist.
- Overwrite the content if the file already exists.
- Do not import any module.

### 2. Append to a file

- Function `append_write` appends a string at the end of a text file (UTF8) and returns the number of characters added.
- Use the `with` statement.
- Do not manage file permissions or exceptions.
- Do not use the `os` module to verify file existence.
- Create the file if it doesn’t exist.

### 3. To JSON string

- Function `to_json_string` returns the JSON representation of an object (string).
- Do not manage exceptions if the object can't be serialized.
- Do not import any module.

### 4. From JSON string to Object

- Function `from_json_string` returns an object (Python data structure) represented by a JSON string.
- Do not manage exceptions if the JSON string doesn’t represent an object.
- Do not import any module.

### 5. Save Object to a file

- Function `save_to_json_file` writes an Object to a text file, using a JSON representation.
- Use the `with` statement.
- Do not manage exceptions if the object can't be serialized.
- Do not manage file permission exceptions.
- Create the file if it doesn’t exist.
- Overwrite the content if the file already exists.
- Do not import any module.

### 6. Load from JSON file

- Function `load_from_json_file` creates an Object from a “JSON file”.
- Use the `with` statement.
- Do not manage exceptions if the JSON string doesn’t represent an object.
- Do not manage file permission exceptions.
- Create the file if it doesn’t exist.
- Use the `from_json_string` function.
