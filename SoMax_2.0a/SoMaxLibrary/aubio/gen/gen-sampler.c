// this file is generated! do not modify
#include "aubio-types.h"

// sampler structure
typedef struct{
    PyObject_HEAD
    // pointer to aubio object
    aubio_sampler_t *o;
    // input parameters
    uint_t samplerate; uint_t hop_size;
    // do input vectors
    fvec_t input;
    // output results
    PyObject *output; fvec_t c_output;
} Py_sampler;

// TODO: add documentation
static char Py_sampler_doc[] = "undefined";

// new sampler
static PyObject *
Py_sampler_new (PyTypeObject * pytype, PyObject * args, PyObject * kwds)
{
    Py_sampler *self;

    uint_t samplerate = 0;
    uint_t hop_size = 0;
    static char *kwlist[] = { "samplerate", "hop_size", NULL };
    if (!PyArg_ParseTupleAndKeywords (args, kwds, "|II", kwlist,
              &samplerate, &hop_size)) {
        return NULL;
    }

    self = (Py_sampler *) pytype->tp_alloc (pytype, 0);
    if (self == NULL) {
        return NULL;
    }

    self->samplerate = Py_aubio_default_samplerate;
    if ((sint_t)samplerate > 0) {
        self->samplerate = samplerate;
    } else if ((sint_t)samplerate < 0) {
        PyErr_SetString (PyExc_ValueError, "can not use negative value for samplerate");
        return NULL;
    }

    self->hop_size = Py_default_vector_length / 2;
    if ((sint_t)hop_size > 0) {
        self->hop_size = hop_size;
    } else if ((sint_t)hop_size < 0) {
        PyErr_SetString (PyExc_ValueError, "can not use negative value for hop_size");
        return NULL;
    }

    return (PyObject *)self;
}

// init sampler
static int
Py_sampler_init (Py_sampler * self, PyObject * args, PyObject * kwds)
{

  self->o = new_aubio_sampler(self->samplerate, self->hop_size);

  // return -1 and set error string on failure
  if (self->o == NULL) {
    PyErr_Format (PyExc_Exception, "failed creating sampler");
    return -1;
  }

  // TODO get internal params after actual object creation?

  // create outputs
  self->output = new_py_fvec(self->hop_size);

  return 0;
}

// del sampler
static void
Py_sampler_del  (Py_sampler * self, PyObject * unused)
{
    Py_DECREF(self->output);
    if (self->o) {
        del_aubio_sampler(self->o);
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

// do sampler
static PyObject*
Py_sampler_do  (Py_sampler * self, PyObject * args)
{
    PyObject *py_input;
    if (!PyArg_ParseTuple (args, "O", &py_input)) {
        return NULL;
    }

    if (!PyAubio_ArrayToCFvec(py_input, &(self->input))) {
        return NULL;
    }

    if (self->input.length != self->hop_size) {
        PyErr_Format (PyExc_ValueError,
            "input size of sampler should be %d, not %d",
            self->hop_size, self->input.length);
        return NULL;
    }

    Py_INCREF(self->output);
    if (!PyAubio_ArrayToCFvec(self->output, &(self->c_output))) {
        return NULL;
    }

    aubio_sampler_do(self->o, &(self->input), &(self->c_output));

    return self->output;
}

static PyMemberDef Py_sampler_members[] = {
  {"samplerate", T_INT, offsetof (Py_sampler, samplerate), READONLY, "TODO documentation"},
  {"hop_size", T_INT, offsetof (Py_sampler, hop_size), READONLY, "TODO documentation"},
  {NULL}, // sentinel
};

// sampler setters

static PyObject *
Pyaubio_sampler_set_playing (Py_sampler *self, PyObject *args)
{
  uint_t err = 0;
  uint_t playing;

  if (!PyArg_ParseTuple (args, "I", &playing)) {
    return NULL;
  }
  err = aubio_sampler_set_playing (self->o, playing);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_sampler_set_playing");
    return NULL;
  }
  Py_RETURN_NONE;
}

// sampler getters

static PyObject *
Pyaubio_sampler_get_playing (Py_sampler *self, PyObject *unused)
{
  uint_t playing = aubio_sampler_get_playing (self->o);
  return (PyObject *)PyLong_FromLong (playing);
}

static PyMethodDef Py_sampler_methods[] = {
  {"set_playing", (PyCFunction) Pyaubio_sampler_set_playing,
    METH_VARARGS, ""},
  {"get_playing", (PyCFunction) Pyaubio_sampler_get_playing,
    METH_NOARGS, ""},
  {NULL} /* sentinel */
};

PyTypeObject Py_samplerType = {
  //PyObject_HEAD_INIT (NULL)
  //0,
  PyVarObject_HEAD_INIT (NULL, 0)
  "aubio.sampler",
  sizeof (Py_sampler),
  0,
  (destructor) Py_sampler_del,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  (ternaryfunc)Py_sampler_do,
  0,
  0,
  0,
  0,
  Py_TPFLAGS_DEFAULT,
  Py_sampler_doc,
  0,
  0,
  0,
  0,
  0,
  0,
  Py_sampler_methods,
  Py_sampler_members,
  0,
  0,
  0,
  0,
  0,
  0,
  (initproc) Py_sampler_init,
  0,
  Py_sampler_new,
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
