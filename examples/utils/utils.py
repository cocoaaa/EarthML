import os
import json
from IPython.display import JSON, display

from pathlib import Path
from pprint import pprint
import pdb

def get_mro(myObj):
    return myObj.__class__.mro()


def nprint(*args, header=True):
    if header:
        print("="*80)
    for arg in args:
        pprint(arg)

def attr_print(myObj):
    attrs = [att for att in dir(dimx) if not att.startswith('_')]
    pprint(attrs)
    
def dict2json(d):
    return JSON(d)

def display_dict2json(d):
    display(JSON(d))

def cols_with_null(df):
    """
    Returns any columnnames with any null value
    Args:
    - df(pandas.DataFrame)
    Returns:
    - cols (list): list of strings, each of which correseponds to the column name
    with any null values
    """
           
    cols = [c for c in df.columns if df[c].isnull().values.any()]
    return cols

def check_url(path):
    import requests
    r = requests.head(path)
    return r.status_code == requests.codes.ok

################################################################################
# Tests
################################################################################
def test_get_mro():
    print( get_mro('somestring') )

def test_nprint():
    nprint(10, 100)
    nprint("line1", "line2")
    nprint(['ele1', 'ele2','ele3'])
    nprint('line1', 'line2', 'line3')

def test_dict2json():
    d = {'user': ['hayley', 'wanting', 'bob', 'yijun'],
         'age': [10,12,11, 9]
        }
    print(d)
    print(dict2json(d))

def test_cols_with_null():
    pass

def test_check_url():
    url = 'http://workflow.isi.edu/MINT/FLDAS/FLDAS_NOAH01_A_EA_D.001/2019/04/FLDAS_NOAH01_A_EA_D.A20190401.001.nc'
    print('url: ', url)
    print('url exists? :', check_url(url))
    
def test_all():
    test_get_mro()
    test_nprint()
    test_dict2json()
    test_cols_with_null()
    test_check_url()
    
    
if __name__ == '__main__':
    test_all()