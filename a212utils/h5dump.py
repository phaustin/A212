#!/usr/bin/env python
from __future__ import print_function
import h5py
import argparse
import types

def print_attrs(name, obj):
    if obj.parent.name=='/':
        print('_'*15)
        print('root group object',repr(obj))
        print('_'*15)
    else:
        print('member of group: ',obj.parent.name,obj)
    try:
        for key, val in obj.attrs.items():
            print("attribute for {:s}    {:s}: {:s}".format(obj.name,key, val))
    except IOError:
        print('this is an HDFStore pandas dataframe')
        print('-'*20)

def dumph5(filename):
    #
    # make sure that have a filename, not an open file
    #
    if isinstance(filename,h5py._hl.files.File):
        raise Exception('need simple filename')
    with  h5py.File(filename,'r') as infile:
        print('+'*20)
        print('found the following top-level items: ')
        for name,object in infile.items():
            print('{}: {}'.format(name,object))
        print('+'*20)
        infile.visititems(print_attrs)
        print('-------------------')
        print("attributes for the root file")
        print('-------------------')
        try:
            for key,value in infile.attrs.items():
                print("attribute name: ",key,"--- value: ",value)
        except IOError:
            pass
        
    return None
        
if __name__ == "__main__":
    #
    # if we are running as main program pass filename as argument
    #
    parser = argparse.ArgumentParser()
    parser.add_argument('h5_file',type=str,help='name of h5 file')
    args=parser.parse_args()
    filename=args.h5_file
    dumph5(filename)

    
    
