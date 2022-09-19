#include <Python.h>


PyObject* add_func(PyObject* self, PyObject* args){
    int x,y;
    PyArg_ParseTuple(args, "ii", &x, &y);
    return PyLong_FromLong((long)(x+y));
};


static struct PyMethodDef methods[] = {
    {"add", add_func, METH_VARARGS, "add two number"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef add = {
    PyModuleDef_HEAD_INIT,
    "111",
    "111",
    -1,
    methods
};

PyMODINIT_FUNC PyInit_add(){
    return PyModule_Create(&add);
}

