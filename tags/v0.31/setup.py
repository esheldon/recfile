from distutils.core import setup, Extension
import numpy
import os


subdir = 'recfile'
sources=['records.cpp', 'records_wrap.cpp']

# platform independent paths
sources = [os.path.join(subdir,f) for f in sources]
module1 = Extension('recfile._records', sources=sources)


setup(name='recfile',
      version='0.10',
      description='This is a test',
      packages=['recfile'],
      ext_modules=[module1],
      py_modules=['records'],
      include_dirs=numpy.get_include())
