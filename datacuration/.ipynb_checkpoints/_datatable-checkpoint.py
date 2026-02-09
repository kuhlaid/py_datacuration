'''
This module will contain functions that help process datatables.
'''
import pandas as pd
from pandas import DataFrame

def dropDfColumn(df, strColumn):
    '''
    Remove a column from a dataframe (in place).

     Parameters
     ----------
     df : dataframe 
     strColumn : string (name of the dataframe column to remove)

     Return
     ----------
     dataframe
    '''
    return df.drop(columns=[strColumn])  # do not use `inplace = True` since it can cause problems since we are outside of this script


def dropDfDupRecords(df, lstColumns, strKeepRecord='last'):
    '''
    Remove duplicate records based on one or more columns in a dataframe (removes records in place). Used pandas dataframe `drop_duplicates` function.

     Parameters
     ----------
     df : dataframe 
     lstColumns : list (list of dataframe columns to search for duplicates)
     strKeepRecord : string (default to 'last' but will take other options for the dataframe drop_duplicates function)

     Return
     ----------
     dataframe
    '''
    return df.drop_duplicates(subset=['HouseholdId'], keep=strKeepRecord) # only keep unique household IDs


def filterByDfColEqTo(df, strColumn, strValue):
    '''
    Filter a dataframe where a column is equal to a value.
    ...

     Parameters
     ----------
     df : dataframe 
     strColumn : str (dataframe column to filter by)
     strValue : string (value to filter by)

     Return
     ----------
     dataframe
    '''
    return df[df[strColumn] == strValue]


def filterByDfColContains(df, strColumn, strValue):
    '''
    Filter a dataframe where a value is in the column.
    ...

     Parameters
     ----------
     df : dataframe 
     strColumn : str (dataframe column to filter by)
     strValue : string (value to filter by)

     Return
     ----------
     dataframe
    '''
    return df[df[strColumn].str.contains(strValue)]


def readCsvStandard(strFilePath):
    '''
    This method ensures that when the CSV files are read, they are treated consistently.
    ...

     Parameters
     ----------
     strFilePath : string (path to the CSV file; NOTE: this should be the absolute path to the file)

     Return
     ----------
     dataframe
    '''
    return pd.read_csv(strFilePath, quoting=1, header=0).convert_dtypes().astype("string").fillna(".")  # we must convert EVERYTHING to strings since we assume the metadata categories (keys and values) will be cast to strings to ensure matches
    # `fillna(".")` adds `.` to empty cells; we need `.convert_dtypes()` to prevent ints from becoming floats and we need to do this BEFORE calling `astype("string") which ensures everything is treated as a string`


    