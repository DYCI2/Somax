// this file is generated! do not modify
#include "aubio-types.h"

// notes structure
typedef struct{
    PyObject_HEAD
    // pointer to aubio object
    aubio_notes_t *o;
    // input parameters
    char_t * method; uint_t buf_size; uint_t hop_size; uint_t samplerate;
    // do input vectors
    fvec_t input;
    // output results
    PyObject *output; fvec_t c_output;
} Py_notes;

// TODO: add documentation
static char Py_notes_doc[] = "undefined";

// new notes
static PyObject *
Py_notes_new (PyTypeObject * pytype, PyObject * args, PyObject * kwds)
{
    Py_notes *self;

    char_t* method = NULL;
    uint_t buf_size = 0;
    uint_t hop_size = 0;
    uint_t samplerate = 0;
    static char *kwlist[] = { "method", "buf_size", "hop_size", "samplerate", NULL };
    if (!PyArg_ParseTupleAndKeywords (args, kwds, "|sIII", kwlist,
              &method, &buf_size, &hop_size, &samplerate)) {
        return NULL;
    }

    self = (Py_notes *) pytype->tp_alloc (pytype, 0);
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

// init notes
static int
Py_notes_init (Py_notes * self, PyObject * args, PyObject * kwds)
{

  self->o = new_aubio_notes(self->method, self->buf_size, self->hop_size, self->samplerate);

  // return -1 and set error string on failure
  if (self->o == NULL) {
    PyErr_Format (PyExc_Exception, "failed creating notes");
    return -1;
  }

  // TODO get internal params after actual object creation?

  // create outputs
  self->output = new_py_fvec(3);

  return 0;
}

// del notes
static void
Py_notes_del  (Py_notes * self, PyObject * unused)
{
    Py_DECREF(self->output);
    if (self->o) {
        del_aubio_notes(self->o);
    }
    Py_TYPE(self)->tp_free((PyObject *) self);
}

// do notes
static PyObject*
Py_notes_do  (Py_notes * self, PyObject * args)
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
            "input size of notes should be %d, not %d",
            self->hop_size, self->input.length);
        return NULL;
    }

    Py_INCREF(self->output);
    if (!PyAubio_ArrayToCFvec(self->output, &(self->c_output))) {
        return NULL;
    }

    aubio_notes_do(self->o, &(self->input), &(self->c_output));

    return self->output;
}

static PyMemberDef Py_notes_members[] = {
  {"method", T_STRING, offsetof (Py_notes, method), READONLY, "TODO documentation"},
  {"buf_size", T_INT, offsetof (Py_notes, buf_size), READONLY, "TODO documentation"},
  {"hop_size", T_INT, offsetof (Py_notes, hop_size), READONLY, "TODO documentation"},
  {"samplerate", T_INT, offsetof (Py_notes, samplerate), READONLY, "TODO documentation"},
  {NULL}, // sentinel
};

// notes setters

// notes getters

static PyMethodDef Py_notes_methods[] = {
  {NULL} /* sentinel */
};

PyTypeObject Py_notesType = {
  //PyObject_HEAD_INIT (NULL)
  //0,
  PyVarObject_HEAD_INIT (NULL, 0)
  "aubio.notes",
  sizeof (Py_notes),
  0,
  (destructor) Py_notes_del,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  (ternaryfunc)Py_notes_do,
  0,
  0,
  0,
  0,
  Py_TPFLAGS_DEFAULT,
  Py_notes_doc,
  0,
  0,
  0,
  0,
  0,
  0,
  Py_notes_methods,
  Py_notes_members,
  0,
  0,
  0,
  0,
  0,
  0,
  (initproc) Py_notes_init,
  0,
  Py_notes_new,
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
