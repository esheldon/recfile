from distutils.core import setup, Extension
import numpy
import os

#module1 = Extension('readfields._readfields2', 
#                    sources=['readfields/src/readfields2.cpp',
#                             'readfields/src/readfields2_wrap.cpp'])

module1 = Extension('recfile._records', 
                    sources=['recfile/records.cpp',
                             'recfile/records_wrap.cpp'])


setup(name='recfile',
      version='0.91',
      description='This is a test',
      packages=['recfile'],
      ext_modules=[module1],
      py_modules=['records'],
      include_dirs=numpy.get_include())
