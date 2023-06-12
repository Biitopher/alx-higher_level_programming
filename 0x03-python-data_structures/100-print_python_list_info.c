#include <stdio.h>

/*
 * print_python_list_info - prints python list info
 * @p: list to be printed
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;
size = PyList_Size(p);
Py_ssize_t allocated = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", allocated);

printf("[*] Element 0: %s\n", Py_TYPE(PyList_GetItem(p, 0))->tp_name);
printf("       Address: %p\n", (void *)PyList_GetItem(p, 0));

for (i = 1; i < size; i++)
{
item = PyList_GetItem(p, i);
printf("[*] Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
printf("       Address: %p\n", (void *)item);
}
}
