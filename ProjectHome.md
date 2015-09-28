# Project Description #

This is a python extension module for reading from and writing to files with fixed length records.  Data are read into or written from numerical python arrays (numpy).  Files can be binary or text files with fixed delimiter, such as csv, tab, or white space.

The extension is a C++ class wrapped using SWIG.

This extension is especially useful when the structure of the file can be determined at run-time, for example from an ascii header.  One implementation of such a format is the SFile module in the [esutil](http://code.google.com/p/esutil/) python package.

## Update history ##
v0.41: bug fix in write()

v0.40: Cleaned up code and documentation, made UPS installation optional.  To install the ups directory, use
> `python setup.py with_ups install --prefix=/some/path`

v0.31:  Major overhaul, adding SFile class and slicing notation for reading.

## Restrictions ##

Still not yet well tested on windows.

## Examples: ##
```
        import recfile

        # Read from a binary file.  If nrows= keyword is not sent, the
        # number of rows will be determined from the file

        file='test.bin'
        dtype=[('x','f8'),('y','i8'),('index','i8'),('flux','5f4')]

        robj = recfile.Open(file, dtype=dtype)

        # read all rows and columns
        data = robj[:]
        data = robj.read()

        # read a subset of rows. Can be a slice or sequence/array.
        data = robj[ 3500:5238 ]
        row_list = [3,25,88]
        data = robj[row_list]
        data = robj.read(rows=row_list)

        # get every 3rd in a slice
        data = robj[ 10:1234:3 ]


        # read a subset of columns.

        # In bracket notation, you must specify rows to read the data.
        data = robj['x'][:]
        field_list = ['x','y']
        data = robj[field_list][row_list]
   
        # alternative syntax
        data = robj['index'].read()
        data = robj.read(columns=column_list)
        data = robj.read(fields=column_list)    # columns/fields are synonyms


        # Read from a CSV file of the same structure, and only read a subset 
        # of the data.  Specifying nrows is not necessary but can speed things up.
        rows2get=[2335,122332,1550021]
        fields2get='field2'
        robj = recfile.Open('test.csv', delim=",", dtype=dtype, nrows=98321)

        data = robj[['x','y']][500:600]
        data = robj.read(rows=rows2get, fields=fields2get)

        # Write a numpy array to a file, with ability to
        # append.  The dtype of the arrays must match upon
        # successive calls to write().

        r = recfile.Open('test.csv', "w", ",")
        r.write(my_array)

        # append more rows
        r.write(second_array)
```