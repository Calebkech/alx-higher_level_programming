#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @python_obj: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *python_obj)
{
    char *byte_string;
    long int byte_size, i, limit;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(python_obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    byte_size = ((PyVarObject *)(python_obj))->ob_size;
    byte_string = ((PyBytesObject *)python_obj)->ob_sval;

    printf("  size: %ld\n", byte_size);
    printf("  trying string: %s\n", byte_string);

    if (byte_size >= 10)
        limit = 10;
    else
        limit = byte_size + 1;

    printf("  first %ld bytes:", limit);

    for (i = 0; i < limit; i++)
        if (byte_string[i] >= 0)
            printf(" %02x", byte_string[i]);
        else
            printf(" %02x", 256 + byte_string[i]);

    printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @python_obj: Python Object
 * Return: no return
 */
void print_python_list(PyObject *python_obj)
{
    long int list_size, i;
    PyListObject *python_list;
    PyObject *element_obj;

    list_size = ((PyVarObject *)(python_obj))->ob_size;
    python_list = (PyListObject *)python_obj;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", list_size);
    printf("[*] Allocated = %ld\n", python_list->allocated);

    for (i = 0; i < list_size; i++)
    {
        element_obj = ((PyListObject *)python_obj)->ob_item[i];
        printf("Element %ld: %s\n", i, ((element_obj)->ob_type)->tp_name);
        if (PyBytes_Check(element_obj))
            print_python_bytes(element_obj);
    }
}
