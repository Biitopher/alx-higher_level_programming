#include <Python.h>

/**
* print_python_list_info - prints python list info
* @p: list parameter to be printed
*
* Return: Nothing
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = x;
	Py_ssize_t  = PyList_Size(p);

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (x = 0; x < size; x++)
	{
		printf("Element %ld: %s\n", x, Py_TYPE(PyList_GetItem(p, x))->tp_name);
	}
}
