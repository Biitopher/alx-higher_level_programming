#include <Python.h>

/**
* print_python_list_info - prints python list info
* @p: list parameter to be printed
*
* Return: Nothing
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t  = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	PyObject *item = PyList_GetItem(p, x);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);
	for (x = 0; x < size; x++)
	{
		printf("Element %ld: %s\n", x, Py_TYPE(item)->tp_name);
	}
}
