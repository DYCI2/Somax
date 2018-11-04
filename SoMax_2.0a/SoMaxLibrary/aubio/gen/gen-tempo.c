// this file is generated! do not modify
#include "aubio-types.h"

// tempo structure
typedef struct{
    PyObject_HEAD
    // pointer to aubio object
    aubio_tempo_t *o;
    // input parameters
    char_t * method; uint_t buf_size; uint_t hop_size; uint_t samplerate;
    // do input vectors
    fvec_t input;
    // output results
    PyObject *tempo; fvec_t c_tempo;
} Py_tempo;

// TODO: add documentation
static char Py_tempo_doc[] = "undefined";

// new tempo
static PyObject *
Py_tempo_new (PyTypeObject * pytype, PyObject * args, PyObject * kwds)
{
    Py_tempo *self;

    char_t* method = NULL;
    uint_t buf_size = 0;
    uint_t hop_size = 0;
    uint_t samplerate = 0;
    static char *kwlist[] = { "method", "buf_size", "hop_size", "samplerate", NULL };
    if (!PyArg_ParseTupleAndKeywords (args, kwds, "|sIII", kwlist,
              &method, &buf_size, &hop_size, &samplerate)) {
        return NULL;
    }

    self = (Py_tempo *) pytype->tp_alloc (pytype, 0);
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

// init tempo
static int
Py_tempo_init (Py_tempo * self, PyObject * args, PyObject * kwds)
{

  self->o = new_aubio_tempo(self->method, self->buf_size, self->hop_size, self->samplerate);

  // return -1 and set error string on failure
  if (self->o == NULL) {
    PyErr_Format (PyExc_Exception, "failed creating tempo");
    return -1;
  }

  // TODO get internal params after actual object creation?

  // create outputs
  self->tempo = new_py_fvec(1);

  return 0;
}

// del tempo
static void
Py_tempo_del  (Py_tempo * self, PyObject * unused)
{
    Py_DECREF(self->tempo);
    if (self->o) {
        del_aubio_tempo(self->o);
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

// do tempo
static PyObject*
Py_tempo_do  (Py_tempo * self, PyObject * args)
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
            "input size of tempo should be %d, not %d",
            self->hop_size, self->input.length);
        return NULL;
    }

    Py_INCREF(self->tempo);
    if (!PyAubio_ArrayToCFvec(self->tempo, &(self->c_tempo))) {
        return NULL;
    }

    aubio_tempo_do(self->o, &(self->input), &(self->c_tempo));

    return self->tempo;
}

static PyMemberDef Py_tempo_members[] = {
  {"method", T_STRING, offsetof (Py_tempo, method), READONLY, "TODO documentation"},
  {"buf_size", T_INT, offsetof (Py_tempo, buf_size), READONLY, "TODO documentation"},
  {"hop_size", T_INT, offsetof (Py_tempo, hop_size), READONLY, "TODO documentation"},
  {"samplerate", T_INT, offsetof (Py_tempo, samplerate), READONLY, "TODO documentation"},
  {NULL}, // sentinel
};

// tempo setters

static PyObject *
Pyaubio_tempo_set_silence (Py_tempo *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t silence;

  if (!PyArg_ParseTuple (args, "f", &silence)) {
    return NULL;
  }
  err = aubio_tempo_set_silence (self->o, silence);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_tempo_set_silence");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_tempo_set_threshold (Py_tempo *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t threshold;

  if (!PyArg_ParseTuple (args, "f", &threshold)) {
    return NULL;
  }
  err = aubio_tempo_set_threshold (self->o, threshold);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_tempo_set_threshold");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_tempo_set_tatum_signature (Py_tempo *self, PyObject *args)
{
  uint_t err = 0;
  uint_t tatum_signature;

  if (!PyArg_ParseTuple (args, "I", &tatum_signature)) {
    return NULL;
  }
  err = aubio_tempo_set_tatum_signature (self->o, tatum_signature);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_tempo_set_tatum_signature");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_tempo_set_delay (Py_tempo *self, PyObject *args)
{
  uint_t err = 0;
  sint_t delay;

  if (!PyArg_ParseTuple (args, "I", &delay)) {
    return NULL;
  }
  err = aubio_tempo_set_delay (self->o, delay);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_tempo_set_delay");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_tempo_set_delay_s (Py_tempo *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t delay_s;

  if (!PyArg_ParseTuple (args, "f", &delay_s)) {
    return NULL;
  }
  err = aubio_tempo_set_delay_s (self->o, delay_s);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_tempo_set_delay_s");
    return NULL;
  }
  Py_RETURN_NONE;
}

static PyObject *
Pyaubio_tempo_set_delay_ms (Py_tempo *self, PyObject *args)
{
  uint_t err = 0;
  smpl_t delay_ms;

  if (!PyArg_ParseTuple (args, "f", &delay_ms)) {
    return NULL;
  }
  err = aubio_tempo_set_delay_ms (self->o, delay_ms);

  if (err > 0) {
    PyErr_SetString (PyExc_ValueError, "error running aubio_tempo_set_delay_ms");
    return NULL;
  }
  Py_RETURN_NONE;
}

// tempo getters

static PyObject *
Pyaubio_tempo_get_last (Py_tempo *self, PyObject *unused)
{
  uint_t last = aubio_tempo_get_last (self->o);
  return (PyObject *)PyLong_FromLong (last);
}

static PyObject *
Pyaubio_tempo_get_last_s (Py_tempo *self, PyObject *unused)
{
  smpl_t last_s = aubio_tempo_get_last_s (self->o);
  return (PyObject *)PyFloat_FromDouble (last_s);
}

static PyObject *
Pyaubio_tempo_get_last_ms (Py_tempo *self, PyObject *unused)
{
  smpl_t last_ms = aubio_tempo_get_last_ms (self->o);
  return (PyObject *)PyFloat_FromDouble (last_ms);
}

static PyObject *
Pyaubio_tempo_get_silence (Py_tempo *self, PyObject *unused)
{
  smpl_t silence = aubio_tempo_get_silence (self->o);
  return (PyObject *)PyFloat_FromDouble (silence);
}

static PyObject *
Pyaubio_tempo_get_threshold (Py_tempo *self, PyObject *unused)
{
  smpl_t threshold = aubio_tempo_get_threshold (self->o);
  return (PyObject *)PyFloat_FromDouble (threshold);
}

static PyObject *
Pyaubio_tempo_get_period (Py_tempo *self, PyObject *unused)
{
  smpl_t period = aubio_tempo_get_period (self->o);
  return (PyObject *)PyFloat_FromDouble (period);
}

static PyObject *
Pyaubio_tempo_get_period_s (Py_tempo *self, PyObject *unused)
{
  smpl_t period_s = aubio_tempo_get_period_s (self->o);
  return (PyObject *)PyFloat_FromDouble (period_s);
}

static PyObject *
Pyaubio_tempo_get_bpm (Py_tempo *self, PyObject *unused)
{
  smpl_t bpm = aubio_tempo_get_bpm (self->o);
  return (PyObject *)PyFloat_FromDouble (bpm);
}

static PyObject *
Pyaubio_tempo_get_confidence (Py_tempo *self, PyObject *unused)
{
  smpl_t confidence = aubio_tempo_get_confidence (self->o);
  return (PyObject *)PyFloat_FromDouble (confidence);
}

static PyObject *
Pyaubio_tempo_get_last_tatum (Py_tempo *self, PyObject *unused)
{
  smpl_t last_tatum = aubio_tempo_get_last_tatum (self->o);
  return (PyObject *)PyFloat_FromDouble (last_tatum);
}

static PyObject *
Pyaubio_tempo_get_delay (Py_tempo *self, PyObject *unused)
{
  uint_t delay = aubio_tempo_get_delay (self->o);
  return (PyObject *)PyLong_FromLong (delay);
}

static PyObject *
Pyaubio_tempo_get_delay_s (Py_tempo *self, PyObject *unused)
{
  smpl_t delay_s = aubio_tempo_get_delay_s (self->o);
  return (PyObject *)PyFloat_FromDouble (delay_s);
}

static PyObject *
Pyaubio_tempo_get_delay_ms (Py_tempo *self, PyObject *unused)
{
  smpl_t delay_ms = aubio_tempo_get_delay_ms (self->o);
  return (PyObject *)PyFloat_FromDouble (delay_ms);
}

static PyMethodDef Py_tempo_methods[] = {
  {"set_silence", (PyCFunction) Pyaubio_tempo_set_silence,
    METH_VARARGS, ""},
  {"set_threshold", (PyCFunction) Pyaubio_tempo_set_threshold,
    METH_VARARGS, ""},
  {"set_tatum_signature", (PyCFunction) Pyaubio_tempo_set_tatum_signature,
    METH_VARARGS, ""},
  {"set_delay", (PyCFunction) Pyaubio_tempo_set_delay,
    METH_VARARGS, ""},
  {"set_delay_s", (PyCFunction) Pyaubio_tempo_set_delay_s,
    METH_VARARGS, ""},
  {"set_delay_ms", (PyCFunction) Pyaubio_tempo_set_delay_ms,
    METH_VARARGS, ""},
  {"get_last", (PyCFunction) Pyaubio_tempo_get_last,
    METH_NOARGS, ""},
  {"get_last_s", (PyCFunction) Pyaubio_tempo_get_last_s,
    METH_NOARGS, ""},
  {"get_last_ms", (PyCFunction) Pyaubio_tempo_get_last_ms,
    METH_NOARGS, ""},
  {"get_silence", (PyCFunction) Pyaubio_tempo_get_silence,
    METH_NOARGS, ""},
  {"get_threshold", (PyCFunction) Pyaubio_tempo_get_threshold,
    METH_NOARGS, ""},
  {"get_period", (PyCFunction) Pyaubio_tempo_get_period,
    METH_NOARGS, ""},
  {"get_period_s", (PyCFunction) Pyaubio_tempo_get_period_s,
    METH_NOARGS, ""},
  {"get_bpm", (PyCFunction) Pyaubio_tempo_get_bpm,
    METH_NOARGS, ""},
  {"get_confidence", (PyCFunction) Pyaubio_tempo_get_confidence,
    METH_NOARGS, ""},
  {"get_last_tatum", (PyCFunction) Pyaubio_tempo_get_last_tatum,
    METH_NOARGS, ""},
  {"get_delay", (PyCFunction) Pyaubio_tempo_get_delay,
    METH_NOARGS, ""},
  {"get_delay_s", (PyCFunction) Pyaubio_tempo_get_delay_s,
    METH_NOARGS, ""},
  {"get_delay_ms", (PyCFunction) Pyaubio_tempo_get_delay_ms,
    METH_NOARGS, ""},
  {NULL} /* sentinel */
};

PyTypeObject Py_tempoType = {
  //PyObject_HEAD_INIT (NULL)
  //0,
  PyVarObject_HEAD_INIT (NULL, 0)
  "aubio.tempo",
  sizeof (Py_tempo),
  0,
  (destructor) Py_tempo_del,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  (ternaryfunc)Py_tempo_do,
  0,
  0,
  0,
  0,
  Py_TPFLAGS_DEFAULT,
  Py_tempo_doc,
  0,
  0,
  0,
  0,
  0,
  0,
  Py_tempo_methods,
  Py_tempo_members,
  0,
  0,
  0,
  0,
  0,
  0,
  (initproc) Py_tempo_init,
  0,
  Py_tempo_new,
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
