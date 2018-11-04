// this file is generated! do not modify
#include "aubio-types.h"

// pitch structure
typedef struct{
    PyObject_HEAD
    // pointer to aubio object
    aubio_pitch_t *o;
    // input parameters
    char_t * method; uint_t buf_size; uint_t hop_size; uint_t samplerate;
    // do input vectors
    fvec_t in;
    // output results
    PyObject *out; fvec_t c_out;
} Py_pitch;

// TODO: add documentation
static char Py_pitch_doc[] = "undefined";

// new pitch
static PyObject *
Py_pitch_new (PyTypeObject * pytype, PyObject * args, PyObject * kwds)
{
    Py_pitch *self;

    char_t* method = NULL;
    uint_t buf_size = 0;
    uint_t hop_size = 0;
    uint_t samplerate = 0;
    static char *kwlist[] = { "method", "buf_size", "hop_size", "samplerate", NULL };
    if (!PyArg_ParseTupleAndKeywords (args, kwds, "|sIII", kwlist,
              &method, &buf_size, &hop_size, &samplerate)) {
        return NULL;
    }

    self = (Py_pitch *) pytype->tp_alloc (pytype, 0);
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

// init pitch
static int
Py_pitch_init (Py_pitch * self, PyObject * args, PyObject * kwds)
{

  self->o = new_aubio_pitch(self->method, self->buf_size, self->hop_size, self->samplerate);

  // return -1 and set error string on failure
  if (self->o == NULL) {
    PyErr_Format (PyExc_Exception, "failed creating pitch");
    return -1;
  }

  // TODO get internal params after actual object creation?

  // create outputs
  self->out = new_py_fvec(1);

  return 0;
}

// del pitch
static void
Py_pitch_del  (Py_pitch * self, PyObject * unused)
{
    Py_DECREF(self->out);
    if (self->o) {
        del_aubio_pitch(self->o);
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

// do pitch
static PyObject*
Py_pitch_do  (Py_pitch * self, PyObject * args)
{
    PyObject *py_in;
    if (!PyArg_ParseTuple (args, "O", &py_in)) {
        return NULL;
    }

    if (!PyAubio_ArrayToCFvec(py_in, &(self->in))) {
        return NULL;
    }

    if (self->in.length != self->hop_size) {
        PyErr_Format (PyExc_ValueError,
            "input size of pitch should be %d, not %d",
            self->hop_size, self->in.length);
        return NULL;
    }

    Py_INCREF(self->out);
    if (!PyAubio_ArrayToCFvec(self->out, &(self->c_out))) {
        return NULL;
    }

    aubio_pitch_do(self->o, &(self->in), &(self->c_out));

    return self->out;
}

static PyMemberDef Py_pitch_members[] = {
  {"method", T_STRING, offsetof (Py_pitch, method), READONLY, "TODO documentation"},
  {"buf_size", T_INT, offsetof (Py_pitch, buf_size), READONLY, "TODO documentation"},
  {"hop_size", T_INT, offsetof (Py_pitch, hop_size), READONLY, "TODO documentation"},
  {"samplerate", T_INT, offsetof (Py_pitch, samplerate), READONLY, "TODO documentation"},
  {NULL}, // sentinel
};

// pitch setters

static PyObject *
Pyaubio_pitch_set_tolerance (Py_pitch *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t tolerance;

  if (!PyArg_ParseTuple (args, "f", &tolerance)) {
    return NULL;
  }
  err = aubio_pitch_set_tolerance (self->o, tolerance);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_pitch_set_tolerance");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_pitch_set_unit (Py_pitch *self, PyObject *args)
{
  uint_t err = 0;
  char_t* unit;

  if (!PyArg_ParseTuple (args, "s", &unit)) {
    return NULL;
  }
  err = aubio_pitch_set_unit (self->o, unit);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_pitch_set_unit");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_pitch_set_silence (Py_pitch *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t silence;

  if (!PyArg_ParseTuple (args, "f", &silence)) {
    return NULL;
  }
  err = aubio_pitch_set_silence (self->o, silence);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_pitch_set_silence");
    return NULL;
  }
  Py_RETURN_NONE;
}

// pitch getters

static PyObject *
Pyaubio_pitch_get_silence (Py_pitch *self, PyObject *unused)
{
  smpl_t silence = aubio_pitch_get_silence (self->o);
  return (PyObject *)PyFloat_FromDouble (silence);
}

static PyObject *
Pyaubio_pitch_get_confidence (Py_pitch *self, PyObject *unused)
{
  smpl_t confidence = aubio_pitch_get_confidence (self->o);
  return (PyObject *)PyFloat_FromDouble (confidence);
}

static PyMethodDef Py_pitch_methods[] = {
  {"set_tolerance", (PyCFunction) Pyaubio_pitch_set_tolerance,
    METH_VARARGS, ""},
  {"set_unit", (PyCFunction) Pyaubio_pitch_set_unit,
    METH_VARARGS, ""},
  {"set_silence", (PyCFunction) Pyaubio_pitch_set_silence,
    METH_VARARGS, ""},
  {"get_silence", (PyCFunction) Pyaubio_pitch_get_silence,
    METH_NOARGS, ""},
  {"get_confidence", (PyCFunction) Pyaubio_pitch_get_confidence,
    METH_NOARGS, ""},
  {NULL} /* sentinel */
};

PyTypeObject Py_pitchType = {
  //PyObject_HEAD_INIT (NULL)
  //0,
  PyVarObject_HEAD_INIT (NULL, 0)
  "aubio.pitch",
  sizeof (Py_pitch),
  0,
  (destructor) Py_pitch_del,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  (ternaryfunc)Py_pitch_do,
  0,
  0,
  0,
  0,
  Py_TPFLAGS_DEFAULT,
  Py_pitch_doc,
  0,
  0,
  0,
  0,
  0,
  0,
  Py_pitch_methods,
  Py_pitch_members,
  0,
  0,
  0,
  0,
  0,
  0,
  (initproc) Py_pitch_init,
  0,
  Py_pitch_new,
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
