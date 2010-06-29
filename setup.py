from distutils.core import setup, Extension
import numpy
import os
import sys


subdir = 'recfile'
sources=['records.cpp', 'records_wrap.cpp']

# platform independent paths
sources = [os.path.join(subdir,f) for f in sources]
module1 = Extension('recfile._records', sources=sources)

# create the ups table
pyvers='%s.%s' % sys.version_info[0:2]
d1='lib/python%s/site-packages' % pyvers
d2='lib64/python%s/site-packages' % pyvers

if not os.path.exists('ups'):
    os.mkdir('ups')
tablefile=open('ups/recfile.table','w')
tab="""
setupOptional("python")
setupOptional("numpy")
envPrepend(PYTHONPATH,${PRODUCT_DIR}/%s)
envPrepend(PYTHONPATH,${PRODUCT_DIR}/%s)
""" % (d1,d2)
tablefile.write(tab)
tablefile.close()



setup(name='recfile',
      description='A class for reading and writing files with fixed length records',
      url='http://code.google.com/p/recfile/',
      packages=['recfile'],
      ext_modules=[module1],
      py_modules=['records'],
      data_files=[('ups',['ups/recfile.table'])],
      include_dirs=numpy.get_include())
