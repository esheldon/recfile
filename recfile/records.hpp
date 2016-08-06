#include <Python.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <stdexcept>
#include <stdint.h>
#include "numpy/arrayobject.h"

#ifndef _readfields_2_h
#define _readfields_2_h

using namespace std;


class Records {
    public:
	/*
		Records() throw (const char*);

        Records(PyObject* fileobj, 
				const char* mode,
				PyObject* delim) throw (const char *);

		PyObject* Open(PyObject* fileobj, 
				const char* mode,
				PyObject* delim) throw (const char *);
				*/

		Records(const char* filename, 
				const char* mode, // mode won't be used if file is object
				PyObject* delim=NULL, 
				PyObject* dtype=NULL,
				long long nrows=-9999,
                long offset=0,
                int bracket_arrays=0) throw (const char *);

        ~Records();

		// Some documentation.  SWIG can use this to make a python doc
		// string
		PyObject* Read(
				PyObject* rows=NULL,
				PyObject* fields=NULL) throw (const char*);

        PyObject* ReadSlice(long long row1, long long row2, long long step) throw (const char*);


		PyObject* Write(
				PyObject* obj, 
				bool padnull=false,
				bool ignorenull=false) throw (const char *);


		void Close() throw (const char*);

        PyObject* write_string(PyObject* obj) throw (const char* );
        PyObject* update_row_count(long nrows) throw (const char* );


        // new style

        PyObject* read_column(PyObject* arrayobj,
                              long colnum,
                              PyObject* input_rows) throw (const char* );

        //PyObject* read_columns(PyObject* arrayobj,
        //                       PyObject* colnums,
        //                       PyObject* rows) throw (const char* );
    private:

        // new style
        npy_intp get_nrows_to_read(PyObject* rows);
        npy_intp get_ncols_to_read(PyObject* rows);

        void scan_column_values(long long fnum, char* buff);
        void read_ascii_bytes(long long colnum, char* buff);
        void read_from_text_column(long long colnum, char* buff);
        void read_from_binary_column(long long colnum, char* buff);

        PyObject* _read_binary_column(PyObject* arrayobj,
                                      long colnum,
                                      PyObject* input_rows) throw (const char* );
        PyObject* _read_text_column(PyObject* arrayobj,
                                    long colnum,
                                    PyObject* input_rows) throw (const char* );

        PyObject* _read_binary_columns(PyObject* arrayobj,
                                       long colnum,
                                       PyObject* input_rows) throw (const char* );

        PyObject* _read_binary_columns(PyObject* arrayobj,
                                       PyObject* colnums,
                                       PyObject* rows) throw (const char* );

		// Move this to public when needed for testing
        PyObject* Test();

        void ensure_writable(void) throw (const char* );
        void ensure_readable(void) throw (const char* );


		// Initialize member variables
		void InitializeVariables();

		// Create an output array.  Data are copied here when reading
		void CreateOutputArray();

		void ReadPrepare();
        npy_intp ProcessSlice(npy_intp row1, npy_intp row2, npy_intp step);
		void ReadFromFile();
		void ReadAllAsBinary();

		void ReadRows();

		void ReadRowsSlice(npy_intp row1, npy_intp step) throw (const char* );

		void ReadRow();
		void ReadAsciiFields();
		void ReadBinaryFields();
		void DoSeek(npy_intp seek_distance);
		//void ReadField(long long fnum);
		void ReadFieldAsBinary(long long fnum);
		void ReadFieldAsAscii(long long fnum);
		void ReadAsciiBytes(long long fnum);
		void ScanVal(long long fnum);
		void SkipField(long long fnum);
		void SkipFieldAsBinary(long long fnum);
		void SkipFieldAsAscii(long long fnum);
		void ReadWholeRowBinary();
		void SkipRows(long long current_row, long long row2read);
		void SkipAsciiRows(long long nskip);
		void SkipBinaryRows(long long nskip);

		void MakeScanFormats(bool add_delim);
		void MakePrintFormats();

		void SubDtype(
				PyObject* descr, 
				PyObject* subnames,
				PyObject** newdescr,
				vector<long long>& matchids);

		PyObject* ExtractSubDescr(
				PyArray_Descr* descr, 
				vector<string>& names);

		void WriteAllAsBinary();
		void WriteRows();
		void WriteField(long long fnum);
        void WriteArrayFieldWithBrackets(long long fnum);
        void _WriteArrayWithBrackets(long long fnum, long long dim);
		void WriteNumberAsAscii(char* buffer, long long type);
		void WriteStringAsAscii(long long fnum);


		void ListStringMatch(
				vector<string> snames,
				PyObject* list, 
				vector<long long>& matchids);

		// Copy some info from a fields["fname"].descr into a tuple This will
		// become part of a list of tuples dtype send to the converter
		PyObject* FieldDescriptorAsTuple(
				PyArray_Descr* fdescr, const char* name);

		long long SequenceCheck(PyObject* obj);

		void CopyFieldInfo(PyArray_Descr* descr);
		void CopyDescrOrderedNames(PyArray_Descr* descr);
		void CopyDescrOrderedOffsets(PyArray_Descr* descr);

		// Must decref this arr no matter what. Use Py_XDECREF in case it
		// is NULL
		PyObject* Object2IntpArray(PyObject* obj);

		// Get the file pointer or open the file if it is a string.  
		void GetFptr(const char* filename, const char* mode);


		// Set the file type based on the delimeter
		void SetFileType();
		// Check the input and if good copy into mDelim string
		void ProcessDelim(PyObject* delim_obj);
		// Check the input descr and get a new reference to it in mTypeDescr
		void ProcessDescr(PyObject* descr);
		// Check the input nrows and copy to mNrows
		void ProcessNrows(long long nrows); 

		// Process the rows keyword and get a version that is an array
		void ProcessRowsToRead(PyObject* rows);
		// Process the fields keyword and extract a sub descr if necessary
		void ProcessFieldsToRead(PyObject* fields);

		void DebugOut(const char* mess);
		void PyDictPrintKeys(PyObject* dict);



		// Data


		// --- means we will initialize 
		// +++ possibly need to decref

		// File name or object
		PyObject* mFileObj;                                    //---
		string mMode;

		// The input type descriptor for each row of the file
		PyObject* mTypeDescr;                                  //--- +++
		// Optional rows to read, default to all.   We will decref
		PyObject* mRowsToRead;                                  //--- +++

		// The return object
		PyArrayObject* mReturnObject;                          //---
		// points to data area
		char* mData;                                           //---

		// A buffer for when skipping ascii
		string mBuffer;

		// Will hold scan and print formats for each data type
		vector<string> mScanFormats;
		vector<string> mPrintFormats;


		FILE* mFptr;                                           //---

		// Delimiter for ascii files
		string mDelim;
        // this can be different when bracket_arrays is sent
        // since we demand commas there
        string mArrayDelim;

		// Reading as binary or ascii?
		bool mReadAsWhitespace;                                //---

		// Read whole file with big fread?
		bool mReadWholeFileBinary;
		// Can read whole rows in binary?
		bool mReadWholeRowBinary;                              //---


		bool mPadNull;
		bool mIgnoreNull;


        // Info about each row of file
        vector<string> mNames;        // Names of all fields in file
        vector<long long> mOffsets;   // offsets of each field in each row
        vector<long long> mSizes;     // size of each field in each row
		vector<long long> mNel;       // number of elements in this field
        vector<long long> mNdim;      // ndim for each field
        vector<vector<long long> > mDims;      // a dims array
		vector<long long> mTypeNums;  // type numbers for each field
        long long mRowSize;           // total size of each row
        vector<long long> mKeep; // boolean, tells if we are keeping each field
		long long mNfields;           // number of fields

        // Info about the fields we are keeping
		PyObject* mKeepTypeDescr;    // descr for the kept fields +++
        vector<string> mKeepNames;   // Names of fields we will retrieve
		// offsets within the kept data structure
        vector<long long> mKeepOffsets;  
        vector<long long> mKeepSizes;      // size of kept fields
		vector<long long> mKeepNel;        // number of elements each field
		vector<long long> mKeepTypeNums;   // type numbers
        long long mKeepRowsize;            // size of kept data structure
        vector<long long> mKeepId;         // index back into above info
		long long mKeepNfields; // number of fields kept

        npy_intp mNrows;             // Total number of rows in file
        npy_intp mNrowsToRead;       // Number of rows we are actually reading.

        long mFileOffset;

		int mFileType;
		int mAction;

		// Action codes
		static const int READ = 1;
		static const int WRITE = 2;

		// File types
		static const int BINARY_FILE = 0;
		static const int ASCII_FILE = 1;

        int mBracketArrays;

		static const bool mDebug=false;
		//static const bool mDebug=true;
};

// Should only be executed once
//import_array();

#endif
