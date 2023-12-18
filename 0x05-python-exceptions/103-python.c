#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - prints data of the PyFloatObject
 * @float_obj: the PyObject representing a float
 */
void print_python_float(PyObject *float_obj)
{
    double value = 0;
    char *string_representation = NULL;

    fflush(stdout);
    printf("[.] float object info\n");

    if (!PyFloat_CheckExact(float_obj))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)float_obj)->ob_fval;
    string_representation = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", string_representation);
}

/**
 * print_python_bytes - prints data of the PyBytesObject
 * @bytes_obj: the PyObject representing bytes
 */
void print_python_bytes(PyObject *bytes_obj)
{
    Py_ssize_t size = 0, i = 0;
    char *byte_string = NULL;

    fflush(stdout);
    printf("[.] bytes object info\n");

    if (!PyBytes_CheckExact(bytes_obj))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(bytes_obj);
    printf("  size: %zd\n", size);
    byte_string = (assert(PyBytes_Check(bytes_obj)), (((PyBytesObject *)(bytes_obj))->ob_sval));
    printf("  trying string: %s\n", byte_string);
    printf("  first %zd bytes:", size < 10 ? size + 1 : 10);

    while (i < size + 1 && i < 10)
    {
        printf(" %02hhx", byte_string[i]);
        i++;
    }

    printf("\n");
}

/**
 * print_python_list - prints data of the PyListObject
 * @list_obj: the PyObject representing a list
 */
void print_python_list(PyObject *list_obj)
{
    Py_ssize_t size = 0;
    PyObject *item;
    int index = 0;

    fflush(stdout);
    printf("[*] Python list info\n");

    if (PyList_CheckExact(list_obj))
    {
        size = PyList_GET_SIZE(list_obj);
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %lu\n", ((PyListObject *)list_obj)->allocated);

        while (index < size)
        {
            item = PyList_GET_ITEM(list_obj, index);
            printf("Element %d: %s\n", index, item->ob_type->tp_name);

            if (PyBytes_Check(item))
                print_python_bytes(item);
            else if (PyFloat_Check(item))
                print_python_float(item);

            index++;
        }
    }
    else
        printf("  [ERROR] Invalid List Object\n");
}
