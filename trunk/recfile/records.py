# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_records', [dirname(__file__)])
        except ImportError:
            import _records
            return _records
        if fp is not None:
            try:
                _mod = imp.load_module('_records', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _records = swig_import_helper()
    del swig_import_helper
else:
    import _records
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Records(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Records, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Records, name)
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        """
        Class
            Records - A class for reading from a file of fixed-length records into
                numerical python arrays. The file can be binary or ASCII.
            An new Records class is instantiated using the Open() method:
                For writing:
                    import records
                    r = records.Open(file/fileobj, mode='w', delim='')
                For reading:
                    import records
                    r = records.Open(file/fileobj, delim='', dtype=None, nrows=-9999)
                    # Arguments can all be given as keywords except the file

                Inputs:
                    file/fileobj:  A string file name or an open file object.
                    mode: The file mode.  Default is 'r' but can be 'u' or 'w'.
                    delim: The delimiter used in the file.  Default is  for 
                        binary files, but can be any string such as ',', '\t', etc.
                    dtype:  A numpy dtype object.  REQUIRED FOR READING. For example:
                        numpy.dtype([('field1', 'i4'),('field2', 'f8')])
                        some_numpy_array.dtype
                    nrows: The number of rows in the file.  REQUIRED FOR READING.

            Class Methods:
                Read(rows=, fields=):
                    Returns the data in a NumPy array.  Specific rows and fields 
                    of the file can be specified with the keywords.  Rows must be
                    sorted and unique.  Can be in any order.
                Write(numpy_array):
                    Write the input numpy array to the file.  The array must have
                    field names defined.

            Examples:
                import numpy
                import records

                # Read from a binary file
                file='test.bin'
                dtype=numpy.dtype([('field1','f8'),('field2','2i4'),('field3','i8')])
                nrows=10000000

                robj = records.Open(file, dtype=dtype, nrows=nrows)
                res=robj.Read()

                # Read from a CSV file of the same structure, and only read a subset 
                # of the data
                rows2get=[2335,122332,1550021]
                fields2get='field2'
                robj = records.Open('test.csv', delim=',', dtype=dtype, nrows=nrows)
                res = robj.Read(rows=rows2get, fields=fields2get)

                # Write a numpy array to a file
                r = records.Open('test.csv', 'w', ',')
                r.Write(my_array)

        Modification history:
            Created: 2008-07-18, Erin Sheldon

        """
        this = _records.new_Records(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _records.delete_Records
    __del__ = lambda self : None;
    def Read(self, rows = None, fields = None):
        """
        Read(rows=None, fields=None)

        A class method for the Records class.  Reads the specified rows
        and fields from the open file and returns the data in a NumPy array.

        Inputs:
            rows:  A sorted unique set of rows.  May be a scala/rlist/array.
              Default is all rows.
            fields: The fields to read.  May be a single string or a list
              of strings.  Can be in any order.  Default is all fields.
        Examples:
            import numpy
            import records
            # Read from a binary file
            file='test.bin'
            dtype=numpy.dtype([('field1','f8'),('field2','2i4'),('field3','i8')])
            nrows=10000000

            robj = records.Open(file, dtype=dtype, nrows=nrows)
            res=robj.Read()

            # Read from a CSV file of the same structure, and only read a subset 
            # of the data
            rows2get=[2335,122332,1550021]
            fields2get='field2'
            robj = records.Open('test.csv', delim=',', dtype=dtype, nrows=nrows)
            res = robj.Read(rows=rows2get, fields=fields2get)
        """
        return _records.Records_Read(self, rows, fields)

    def ReadSlice(self, *args, **kwargs):
        """
        Read(rows=None, fields=None)

        A class method for the Records class.  Reads the specified rows
        and fields from the open file and returns the data in a NumPy array.

        Inputs:
            rows:  A sorted unique set of rows.  May be a scala/rlist/array.
              Default is all rows.
            fields: The fields to read.  May be a single string or a list
              of strings.  Can be in any order.  Default is all fields.
        Examples:
            import numpy
            import records
            # Read from a binary file
            file='test.bin'
            dtype=numpy.dtype([('field1','f8'),('field2','2i4'),('field3','i8')])
            nrows=10000000

            robj = records.Open(file, dtype=dtype, nrows=nrows)
            res=robj.Read()

            # Read from a CSV file of the same structure, and only read a subset 
            # of the data
            rows2get=[2335,122332,1550021]
            fields2get='field2'
            robj = records.Open('test.csv', delim=',', dtype=dtype, nrows=nrows)
            res = robj.Read(rows=rows2get, fields=fields2get)
        """
        return _records.Records_ReadSlice(self, *args, **kwargs)

    def Write(self, *args, **kwargs):
        """
        Write(numpy_array, pad=False)

        A class method for the Records class.  Writes the input numpy array
        to the opened file.

        Inputs:
            array: A NumPy array with fields defined for the records.
        Keywords:
        	padnull=False:  
        		Convert NULL characters to spaces when writing.  Note when
        		read back in these will not compare equal with the original
        		data!  This is useful when writing files to be read in by
        		programs that do not recognize null characters, e.g. sqlite
        		databases.

        	ignorenull=False:
        		Ignore NULL characters entirely when writing strings to ascii
        		files. This is useful when writing files to be read in by
        		programs that do not recognize null characters, e.g. sqlite
        		databases.

        Examples:
            import numpy
            import records
            r = records.Open('test.csv', 'w', ',')
            r.Write(my_array)

        """
        return _records.Records_Write(self, *args, **kwargs)

    def Close(self):
        """
        Close()

        If the file was opened locally, close the file pointer.

        """
        return _records.Records_Close(self)

Records_swigregister = _records.Records_swigregister
Records_swigregister(Records)



