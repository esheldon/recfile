Python code to read and write files with fixed length records.

The data are read from and into numerical python arrays.  Both
binary and text formats are supported.

Examples
---------
```python
#
# reading files
#

# create a numpy data type describing each row in the file

dtype=[('field1','f8'),('field2','2i4'),('field3','i8')]
fname='test.bin'

# you can use the convenience function if you want basic
# functionality

data = recfile.read(fname, dtype)

# you can create a Recfile object for more detailed
# exploration

with Recfile(fname, mode="r", dtype=dtype) as robj:

    # read all data
    data = robj.read()   # function interface
    data = robj[:]       # slice notation

    # read a subset of rows using slice notation
    data = robj[3500:5238]
    data = robj[ 10:1234:3 ]


    # specifying a set of rows explicitly; can be a list or
    # array
    row_list = [35,88,217]

    data = robj[row_list]
    data = robj.read(rows=row_list)

    # read a subset of columns.
    column_list = ['field2','field3']
    data = robj.read(columns=column_list)

    # In bracket notation, you must specify rows to read the data.

    data = robj['field2'][:]
    data = robj[column_list][rowlist]
    data = robj['field3'].read()

#
# reading text data.  You need to specify a delimiter, e.g. "," for csv
# " " for whitespace delimited, etc.

with Recfile('test.csv', delim=',', dtype=dtype) as robj:

    rows2get=[2335,122332,1550021]
    fields2get='field2'

    data = robj.read(rows=rows2get, fields=fields2get)
    data = robj[fields2get][rows2get]

# using the convenience function
data = recfile.read('test.csv', delim=',', dtype=dtype)

#
# writing files
#

from recfile import Recfile
with Recfile(fname, mode='w') as robj:
    robj.write(data1)
    robj.write(data2) # append data

# for updating use mode='r+'


# you can also use close() if you are not in a context

robj = Recfile(fname, mode='w')
robj.write(data1)
robj.close()

# you can also use a convenience function to write

recfile.write(fname, data)
```
