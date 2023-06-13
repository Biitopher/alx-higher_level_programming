#include <python.h>

/*
 * print_python_list_info - prints python list info
 * @p: list parameter to be printed
 * Return: Nothing
 */

void print_python_list_info(PyObject *p)
{
Py_ssize_t x;
size = PyList_Size(p);
Py_ssize_t allocated = ((PyListObject *)p)->allocated;
item = PyList_GetItem(p, x);

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", Py_ssize_t allocated);

for (x = 1; x < size; x++)
{
printf("[*] Element %ld: %s\n", x, Py_TYPE(item)->tp_name);
}
