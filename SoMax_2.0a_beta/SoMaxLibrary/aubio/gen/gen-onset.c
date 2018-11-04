// this file is generated! do not modify
#include "aubio-types.h"

// onset structure
typedef struct{
    PyObject_HEAD
    // pointer to aubio object
    aubio_onset_t *o;
    // input parameters
    char_t * method; uint_t buf_size; uint_t hop_size; uint_t samplerate;
    // do input vectors
    fvec_t input;
    // output results
    PyObject *onset; fvec_t c_onset;
} Py_onset;

// TODO: add documentation
static char Py_onset_doc[] = "undefined";

// new onset
static PyObject *
Py_onset_new (PyTypeObject * pytype, PyObject * args, PyObject * kwds)
{
    Py_onset *self;

    char_t* method = NULL;
    uint_t buf_size = 0;
    uint_t hop_size = 0;
    uint_t samplerate = 0;
    static char *kwlist[] = { "method", "buf_size", "hop_size", "samplerate", NULL };
    if (!PyArg_ParseTupleAndKeywords (args, kwds, "|sIII", kwlist,
              &method, &buf_size, &hop_size, &samplerate)) {
        return NULL;
    }

    self = (Py_onset *) pytype->tp_alloc (pytype, 0);
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

    self->hop_size = Py_default_vector_length / 2;
    if ((sint_t)hop_size > 0) {
        self->hop_size = hop_size;
    } else if ((sint_t)hop_size < 0) {
        PyErr_SetString (PyExc_ValueError, "can not use negative value for hop_size");
        return NULL;
    }

    self->samplerate = Py_aubio_default_samplerate;
    if ((sint_t)samplerate > 0) {
        self->samplerate = samplerate;
    } else if ((sint_t)samplerate < 0) {
        PyErr_SetString (PyExc_ValueError, "can not use negative value for samplerate");
        return NULL;
    }

    return (PyObject *)self;
}

// init onset
static int
Py_onset_init (Py_onset * self, PyObject * args, PyObject * kwds)
{

  self->o = new_aubio_onset(self->method, self->buf_size, self->hop_size, self->samplerate);

  // return -1 and set error string on failure
  if (self->o == NULL) {
    PyErr_Format (PyExc_Exception, "failed creating onset");
    return -1;
  }

  // TODO get internal params after actual object creation?

  // create outputs
  self->onset = new_py_fvec(1);

  return 0;
}

// del onset
static void
Py_onset_del  (Py_onset * self, PyObject * unused)
{
    Py_DECREF(self->onset);
    if (self->o) {
        del_aubio_onset(self->o);
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

// do onset
static PyObject*
Py_onset_do  (Py_onset * self, PyObject * args)
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
            "input size of onset should be %d, not %d",
            self->hop_size, self->input.length);
        return NULL;
    }

    Py_INCREF(self->onset);
    if (!PyAubio_ArrayToCFvec(self->onset, &(self->c_onset))) {
        return NULL;
    }

    aubio_onset_do(self->o, &(self->input), &(self->c_onset));

    return self->onset;
}

static PyMemberDef Py_onset_members[] = {
  {"method", T_STRING, offsetof (Py_onset, method), READONLY, "TODO documentation"},
  {"buf_size", T_INT, offsetof (Py_onset, buf_size), READONLY, "TODO documentation"},
  {"hop_size", T_INT, offsetof (Py_onset, hop_size), READONLY, "TODO documentation"},
  {"samplerate", T_INT, offsetof (Py_onset, samplerate), READONLY, "TODO documentation"},
  {NULL}, // sentinel
};

// onset setters

static PyObject *
Pyaubio_onset_set_silence (Py_onset *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t silence;

  if (!PyArg_ParseTuple (args, "f", &silence)) {
    return NULL;
  }
  err = aubio_onset_set_silence (self->o, silence);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_onset_set_silence");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_onset_set_threshold (Py_onset *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t threshold;

  if (!PyArg_ParseTuple (args, "f", &threshold)) {
    return NULL;
  }
  err = aubio_onset_set_threshold (self->o, threshold);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_onset_set_threshold");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_onset_set_minioi (Py_onset *self, PyObject *args)
{
  uint_t err = 0;
  uint_t minioi;

  if (!PyArg_ParseTuple (args, "I", &minioi)) {
    return NULL;
  }
  err = aubio_onset_set_minioi (self->o, minioi);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_onset_set_minioi");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_onset_set_minioi_s (Py_onset *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t minioi_s;

  if (!PyArg_ParseTuple (args, "f", &minioi_s)) {
    return NULL;
  }
  err = aubio_onset_set_minioi_s (self->o, minioi_s);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_onset_set_minioi_s");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_onset_set_minioi_ms (Py_onset *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t minioi_ms;

  if (!PyArg_ParseTuple (args, "f", &minioi_ms)) {
    return NULL;
  }
  err = aubio_onset_set_minioi_ms (self->o, minioi_ms);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_onset_set_minioi_ms");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_onset_set_delay (Py_onset *self, PyObject *args)
{
  uint_t err = 0;
  uint_t delay;

  if (!PyArg_ParseTuple (args, "I", &delay)) {
    return NULL;
  }
  err = aubio_onset_set_delay (self->o, delay);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_onset_set_delay");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_onset_set_delay_s (Py_onset *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t delay_s;

  if (!PyArg_ParseTuple (args, "f", &delay_s)) {
    return NULL;
  }
  err = aubio_onset_set_delay_s (self->o, delay_s);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_onset_set_delay_s");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_onset_set_delay_ms (Py_onset *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t delay_ms;

  if (!PyArg_ParseTuple (args, "f", &delay_ms)) {
    return NULL;
  }
  err = aubio_onset_set_delay_ms (self->o, delay_ms);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_onset_set_delay_ms");
    return NULL;
  }
  Py_RETURN_NONE;
}

// onset getters

static PyObject *
Pyaubio_onset_get_last (Py_onset *self, PyObject *unused)
{
  uint_t last = aubio_onset_get_last (self->o);
  return (PyObject *)PyLong_FromLong (last);
}

static PyObject *
Pyaubio_onset_get_last_s (Py_onset *self, PyObject *unused)
{
  smpl_t last_s = aubio_onset_get_last_s (self->o);
  return (PyObject *)PyFloat_FromDouble (last_s);
}

static PyObject *
Pyaubio_onset_get_last_ms (Py_onset *self, PyObject *unused)
{
  smpl_t last_ms = aubio_onset_get_last_ms (self->o);
  return (PyObject *)PyFloat_FromDouble (last_ms);
}

static PyObject *
Pyaubio_onset_get_silence (Py_onset *self, PyObject *unused)
{
  smpl_t silence = aubio_onset_get_silence (self->o);
  return (PyObject *)PyFloat_FromDouble (silence);
}

static PyObject *
Pyaubio_onset_get_descriptor (Py_onset *self, PyObject *unused)
{
  smpl_t descriptor = aubio_onset_get_descriptor (self->o);
  return (PyObject *)PyFloat_FromDouble (descriptor);
}

static PyObject *
Pyaubio_onset_get_thresholded_descriptor (Py_onset *self, PyObject *unused)
{
  smpl_t thresholded_descriptor = aubio_onset_get_thresholded_descriptor (self->o);
  return (PyObject *)PyFloat_FromDouble (thresholded_descriptor);
}

static PyObject *
Pyaubio_onset_get_minioi (Py_onset *self, PyObject *unused)
{
  uint_t minioi = aubio_onset_get_minioi (self->o);
  return (PyObject *)PyLong_FromLong (minioi);
}

static PyObject *
Pyaubio_onset_get_minioi_s (Py_onset *self, PyObject *unused)
{
  smpl_t minioi_s = aubio_onset_get_minioi_s (self->o);
  return (PyObject *)PyFloat_FromDouble (minioi_s);
}

static PyObject *
Pyaubio_onset_get_minioi_ms (Py_onset *self, PyObject *unused)
{
  smpl_t minioi_ms = aubio_onset_get_minioi_ms (self->o);
  return (PyObject *)PyFloat_FromDouble (minioi_ms);
}

static PyObject *
Pyaubio_onset_get_delay (Py_onset *self, PyObject *unused)
{
  uint_t delay = aubio_onset_get_delay (self->o);
  return (PyObject *)PyLong_FromLong (delay);
}

static PyObject *
Pyaubio_onset_get_delay_s (Py_onset *self, PyObject *unused)
{
  smpl_t delay_s = aubio_onset_get_delay_s (self->o);
  return (PyObject *)PyFloat_FromDouble (delay_s);
}

static PyObject *
Pyaubio_onset_get_delay_ms (Py_onset *self, PyObject *unused)
{
  smpl_t delay_ms = aubio_onset_get_delay_ms (self->o);
  return (PyObject *)PyFloat_FromDouble (delay_ms);
}

static PyObject *
Pyaubio_onset_get_threshold (Py_onset *self, PyObject *unused)
{
  smpl_t threshold = aubio_onset_get_threshold (self->o);
  return (PyObject *)PyFloat_FromDouble (threshold);
}

static PyMethodDef Py_onset_methods[] = {
  {"set_silence", (PyCFunction) Pyaubio_onset_set_silence,
    METH_VARARGS, ""},
  {"set_threshold", (PyCFunction) Pyaubio_onset_set_threshold,
    METH_VARARGS, ""},
  {"set_minioi", (PyCFunction) Pyaubio_onset_set_minioi,
    METH_VARARGS, ""},
  {"set_minioi_s", (PyCFunction) Pyaubio_onset_set_minioi_s,
    METH_VARARGS, ""},
  {"set_minioi_ms", (PyCFunction) Pyaubio_onset_set_minioi_ms,
    METH_VARARGS, ""},
  {"set_delay", (PyCFunction) Pyaubio_onset_set_delay,
    METH_VARARGS, ""},
  {"set_delay_s", (PyCFunction) Pyaubio_onset_set_delay_s,
    METH_VARARGS, ""},
  {"set_delay_ms", (PyCFunction) Pyaubio_onset_set_delay_ms,
    METH_VARARGS, ""},
  {"get_last", (PyCFunction) Pyaubio_onset_get_last,
    METH_NOARGS, ""},
  {"get_last_s", (PyCFunction) Pyaubio_onset_get_last_s,
    METH_NOARGS, ""},
  {"get_last_ms", (PyCFunction) Pyaubio_onset_get_last_ms,
    METH_NOARGS, ""},
  {"get_silence", (PyCFunction) Pyaubio_onset_get_silence,
    METH_NOARGS, ""},
  {"get_descriptor", (PyCFunction) Pyaubio_onset_get_descriptor,
    METH_NOARGS, ""},
  {"get_thresholded_descriptor", (PyCFunction) Pyaubio_onset_get_thresholded_descriptor,
    METH_NOARGS, ""},
  {"get_minioi", (PyCFunction) Pyaubio_onset_get_minioi,
    METH_NOARGS, ""},
  {"get_minioi_s", (PyCFunction) Pyaubio_onset_get_minioi_s,
    METH_NOARGS, ""},
  {"get_minioi_ms", (PyCFunction) Pyaubio_onset_get_minioi_ms,
    METH_NOARGS, ""},
  {"get_delay", (PyCFunction) Pyaubio_onset_get_delay,
    METH_NOARGS, ""},
  {"get_delay_s", (PyCFunction) Pyaubio_onset_get_delay_s,
    METH_NOARGS, ""},
  {"get_delay_ms", (PyCFunction) Pyaubio_onset_get_delay_ms,
    METH_NOARGS, ""},
  {"get_threshold", (PyCFunction) Pyaubio_onset_get_threshold,
    METH_NOARGS, ""},
  {NULL} /* sentinel */
};

PyTypeObject Py_onsetType = {
  //PyObject_HEAD_INIT (NULL)
  //0,
  PyVarObject_HEAD_INIT (NULL, 0)
  "aubio.onset",
  sizeof (Py_onset),
  0,
  (destructor) Py_onset_del,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  (ternaryfunc)Py_onset_do,
  0,
  0,
  0,
  0,
  Py_TPFLAGS_DEFAULT,
  Py_onset_doc,
  0,
  0,
  0,
  0,
  0,
  0,
  Py_onset_methods,
  Py_onset_members,
  0,
  0,
  0,
  0,
  0,
  0,
  (initproc) Py_onset_init,
  0,
  Py_onset_new,
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
