from distutils.core import setup, Extension, Command
import numpy
import os
import sys

import distutils.sysconfig

subdir = 'recfile'
sources=['records.cpp', 'records_wrap.cpp']

# platform independent paths
sources = [os.path.join(subdir,f) for f in sources]
module1 = Extension('recfile._records', sources=sources)

data_files=[]


class AddUPS(Command):
    _data_files = data_files
    user_options=[]
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):

        main_libdir=distutils.sysconfig.get_python_lib()
        pylib_install_subdir = main_libdir.replace(distutils.sysconfig.PREFIX+os.sep,'')

        if not os.path.exists('ups'):
            os.mkdir('ups')
        tablefile=open('ups/recfile.table','w')
        tab="""
        setupOptional("python")
        setupOptional("numpy")
        envPrepend(PYTHONPATH,${PRODUCT_DIR}/%s)
        """ % pylib_install_subdir 
        tablefile.write(tab)
        tablefile.close()

        AddUPS._data_files.append(('ups',['ups/recfile.table']))




description=("A class for reading and writing numpy record arrays "
             "to and from files with fixed length records")

setup(name='recfile',
      version='0.41',
      cmdclass={"with_ups": AddUPS},
      description=description,
      url='http://code.google.com/p/recfile/',
      packages=['recfile'],
      ext_modules=[module1],
      py_modules=['records'],
      data_files=data_files,
      include_dirs=numpy.get_include())
