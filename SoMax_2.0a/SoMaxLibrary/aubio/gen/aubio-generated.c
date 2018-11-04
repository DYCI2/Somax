// this file is generated! do not modify
#include "aubio-types.h"
#include "aubio-generated.h"

int generated_types_ready (void)
{
  return (PyType_Ready(&Py_wavetableType) < 0
     ||  PyType_Ready(&Py_mfccType) < 0
     ||  PyType_Ready(&Py_specdescType) < 0
     ||  PyType_Ready(&Py_samplerType) < 0
     ||  PyType_Ready(&Py_tempoType) < 0
     ||  PyType_Ready(&Py_onsetType) < 0
     ||  PyType_Ready(&Py_pitchType) < 0
     ||  PyType_Ready(&Py_notesType) < 0);
}


void add_generated_objects ( PyObject *m )
{

  Py_INCREF (&Py_wavetableType);
  PyModule_AddObject(m, "wavetable", (PyObject *) & Py_wavetableType);
  Py_INCREF (&Py_mfccType);
  PyModule_AddObject(m, "mfcc", (PyObject *) & Py_mfccType);
  Py_INCREF (&Py_specdescType);
  PyModule_AddObject(m, "specdesc", (PyObject *) & Py_specdescType);
  Py_INCREF (&Py_samplerType);
  PyModule_AddObject(m, "sampler", (PyObject *) & Py_samplerType);
  Py_INCREF (&Py_tempoType);
  PyModule_AddObject(m, "tempo", (PyObject *) & Py_tempoType);
  Py_INCREF (&Py_onsetType);
  PyModule_AddObject(m, "onset", (PyObject *) & Py_onsetType);
  Py_INCREF (&Py_pitchType);
  PyModule_AddObject(m, "pitch", (PyObject *) & Py_pitchType);
  Py_INCREF (&Py_notesType);
  PyModule_AddObject(m, "notes", (PyObject *) & Py_notesType);
}
