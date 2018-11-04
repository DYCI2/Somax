// this file is generated! do not modify
#include "aubio-types.h"

// specdesc structure
typedef struct{
    PyObject_HEAD
    // pointer to aubio object
    aubio_specdesc_t *o;
    // input parameters
    char_t * method; uint_t buf_size;
    // do input vectors
    cvec_t fftgrain;
    // output results
    PyObject *desc; fvec_t c_desc;
} Py_specdesc;

// TODO: add documentation
static char Py_specdesc_doc[] = "undefined";

// new specdesc
static PyObject *
Py_specdesc_new (PyTypeObject * pytype, PyObject * args, PyObject * kwds)
{
    Py_specdesc *self;

    char_t* method = NULL;
    uint_t buf_size = 0;
    static char *kwlist[] = { "method", "buf_size", NULL };
    if (!PyArg_ParseTupleAndKeywords (args, kwds, "|sI", kwlist,
              &method, &buf_size)) {
        return NULL;
    }

    self = (Py_specdesc *) pytype->tp_alloc (pytype, 0);
    if (self == NULL) {
        return NULL;
    }

    self->method = "default";
    if (method != NULL) {
        self->method = method;
    }

    self->buf_size = Py_default_vector_length;
    if ((sint_t)buf_size > 0) {
        self->buf_size = buf_size;
    } else if ((sint_t)buf_size < 0) {
        PyErr_SetString (PyExc_ValueError, "can not use negative value for buf_size");
        return NULL;
    }

    return (PyObject *)self;
}

// init specdesc
static int
Py_specdesc_init (Py_specdesc * self, PyObject * args, PyObject * kwds)
{

  self->o = new_aubio_specdesc(self->method, self->buf_size);

  // return -1 and set error string on failure
  if (self->o == NULL) {
    PyErr_Format (PyExc_Exception, "failed creating specdesc");
    return -1;
  }

  // TODO get internal params after actual object creation?

  // create outputs
  self->desc = new_py_fvec(1);

  return 0;
}

// del specdesc
static void
Py_specdesc_del  (Py_specdesc * self, PyObject * unused)
{
    Py_DECREF(self->desc);
    if (self->o) {
        del_aubio_specdesc(self->o);
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

// do specdesc
static PyObject*
Py_specdesc_do  (Py_specdesc * self, PyObject * args)
{
    PyObject *py_fftgrain;
    if (!PyArg_ParseTuple (args, "O", &py_fftgrain)) {
        return NULL;
    }

    if (!PyAubio_PyCvecToCCvec(py_fftgrain, &(self->fftgrain))) {
        return NULL;
    }

    if (self->fftgrain.length != self->buf_size / 2 + 1) {
        PyErr_Format (PyExc_ValueError,
            "input size of specdesc should be %d, not %d",
            self->buf_size / 2 + 1, self->fftgrain.length);
        return NULL;
    }

    Py_INCREF(self->desc);
    if (!PyAubio_ArrayToCFvec(self->desc, &(self->c_desc))) {
        return NULL;
    }

    aubio_specdesc_do(self->o, &(self->fftgrain), &(self->c_desc));

    return self->desc;
}

static PyMemberDef Py_specdesc_members[] = {
  {"method", T_STRING, offsetof (Py_specdesc, method), READONLY, "TODO documentation"},
  {"buf_size", T_INT, offsetof (Py_specdesc, buf_size), READONLY, "TODO documentation"},
  {NULL}, // sentinel
};

// specdesc setters

// specdesc getters

static PyMethodDef Py_specdesc_methods[] = {
  {NULL} /* sentinel */
};

PyTypeObject Py_specdescType = {
  //PyObject_HEAD_INIT (NULL)
  //0,
  PyVarObject_HEAD_INIT (NULL, 0)
  "aubio.specdesc",
  sizeof (Py_specdesc),
  0,
  (destructor) Py_specdesc_del,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  (ternaryfunc)Py_specdesc_do,
  0,
  0,
  0,
  0,
  Py_TPFLAGS_DEFAULT,
  Py_specdesc_doc,
  0,
  0,
  0,
  0,
  0,
  0,
  Py_specdesc_methods,
  Py_specdesc_members,
  0,
  0,
  0,
  0,
  0,
  0,
  (initproc) Py_specdesc_init,
  0,
  Py_specdesc_new,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
};
