// this file is generated! do not modify
#include "aubio-types.h"

// wavetable structure
typedef struct{
    PyObject_HEAD
    // pointer to aubio object
    aubio_wavetable_t *o;
    // input parameters
    uint_t samplerate; uint_t hop_size;
    // do input vectors
    fvec_t input;
    // output results
    PyObject *output; fvec_t c_output;
} Py_wavetable;

// TODO: add documentation
static char Py_wavetable_doc[] = "undefined";

// new wavetable
static PyObject *
Py_wavetable_new (PyTypeObject * pytype, PyObject * args, PyObject * kwds)
{
    Py_wavetable *self;

    uint_t samplerate = 0;
    uint_t hop_size = 0;
    static char *kwlist[] = { "samplerate", "hop_size", NULL };
    if (!PyArg_ParseTupleAndKeywords (args, kwds, "|II", kwlist,
              &samplerate, &hop_size)) {
        return NULL;
    }

    self = (Py_wavetable *) pytype->tp_alloc (pytype, 0);
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

// init wavetable
static int
Py_wavetable_init (Py_wavetable * self, PyObject * args, PyObject * kwds)
{

  self->o = new_aubio_wavetable(self->samplerate, self->hop_size);

  // return -1 and set error string on failure
  if (self->o == NULL) {
    PyErr_Format (PyExc_Exception, "failed creating wavetable");
    return -1;
  }

  // TODO get internal params after actual object creation?

  // create outputs
  self->output = new_py_fvec(self->hop_size);

  return 0;
}

// del wavetable
static void
Py_wavetable_del  (Py_wavetable * self, PyObject * unused)
{
    Py_DECREF(self->output);
    if (self->o) {
        del_aubio_wavetable(self->o);
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

// do wavetable
static PyObject*
Py_wavetable_do  (Py_wavetable * self, PyObject * args)
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
            "input size of wavetable should be %d, not %d",
            self->hop_size, self->input.length);
        return NULL;
    }

    Py_INCREF(self->output);
    if (!PyAubio_ArrayToCFvec(self->output, &(self->c_output))) {
        return NULL;
    }

    aubio_wavetable_do(self->o, &(self->input), &(self->c_output));

    return self->output;
}

static PyMemberDef Py_wavetable_members[] = {
  {"samplerate", T_INT, offsetof (Py_wavetable, samplerate), READONLY, "TODO documentation"},
  {"hop_size", T_INT, offsetof (Py_wavetable, hop_size), READONLY, "TODO documentation"},
  {NULL}, // sentinel
};

// wavetable setters

static PyObject *
Pyaubio_wavetable_set_playing (Py_wavetable *self, PyObject *args)
{
  uint_t err = 0;
  uint_t playing;

  if (!PyArg_ParseTuple (args, "I", &playing)) {
    return NULL;
  }
  err = aubio_wavetable_set_playing (self->o, playing);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_wavetable_set_playing");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_wavetable_set_freq (Py_wavetable *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t freq;

  if (!PyArg_ParseTuple (args, "f", &freq)) {
    return NULL;
  }
  err = aubio_wavetable_set_freq (self->o, freq);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_wavetable_set_freq");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_wavetable_set_amp (Py_wavetable *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t amp;

  if (!PyArg_ParseTuple (args, "f", &amp)) {
    return NULL;
  }
  err = aubio_wavetable_set_amp (self->o, amp);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_wavetable_set_amp");
    return NULL;
  }
  Py_RETURN_NONE;
}

// wavetable getters

static PyObject *
Pyaubio_wavetable_get_playing (Py_wavetable *self, PyObject *unused)
{
  uint_t playing = aubio_wavetable_get_playing (self->o);
  return (PyObject *)PyLong_FromLong (playing);
}

static PyObject *
Pyaubio_wavetable_get_freq (Py_wavetable *self, PyObject *unused)
{
  smpl_t freq = aubio_wavetable_get_freq (self->o);
  return (PyObject *)PyFloat_FromDouble (freq);
}

static PyObject *
Pyaubio_wavetable_get_amp (Py_wavetable *self, PyObject *unused)
{
  smpl_t amp = aubio_wavetable_get_amp (self->o);
  return (PyObject *)PyFloat_FromDouble (amp);
}

static PyMethodDef Py_wavetable_methods[] = {
  {"set_playing", (PyCFunction) Pyaubio_wavetable_set_playing,
    METH_VARARGS, ""},
  {"set_freq", (PyCFunction) Pyaubio_wavetable_set_freq,
    METH_VARARGS, ""},
  {"set_amp", (PyCFunction) Pyaubio_wavetable_set_amp,
    METH_VARARGS, ""},
  {"get_playing", (PyCFunction) Pyaubio_wavetable_get_playing,
    METH_NOARGS, ""},
  {"get_freq", (PyCFunction) Pyaubio_wavetable_get_freq,
    METH_NOARGS, ""},
  {"get_amp", (PyCFunction) Pyaubio_wavetable_get_amp,
    METH_NOARGS, ""},
  {NULL} /* sentinel */
};

PyTypeObject Py_wavetableType = {
  //PyObject_HEAD_INIT (NULL)
  //0,
  PyVarObject_HEAD_INIT (NULL, 0)
  "aubio.wavetable",
  sizeof (Py_wavetable),
  0,
  (destructor) Py_wavetable_del,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  (ternaryfunc)Py_wavetable_do,
  0,
  0,
  0,
  0,
  Py_TPFLAGS_DEFAULT,
  Py_wavetable_doc,
  0,
  0,
  0,
  0,
  0,
  0,
  Py_wavetable_methods,
  Py_wavetable_members,
  0,
  0,
  0,
  0,
  0,
  0,
  (initproc) Py_wavetable_init,
  0,
  Py_wavetable_new,
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
