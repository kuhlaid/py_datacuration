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
    return df.drop_duplicates(subset=lstColumns, keep=strKeepRecord) # only keep unique household IDs


def subsetDfByList(df, strColumn, lstValues):
    '''
    Returns a subset of a data table based on a list of values in a column.

     Parameters
     ----------
     df : dataframe 
     strColumn : string (name of dataframe column to search for values)
     lstValues : list (list of values to filter the column by)

     Return
     ----------
     dataframe
    '''
    return df[df[strColumn].isin(lstValues)]


def filterByDfColNotNa(df, strColumn):
    '''
    Returns a subset of a data table based on a column values that are not NA or NaN (missing values).

     Parameters
     ----------
     df : dataframe 
     strColumn : string (name of dataframe column to search for values)

     Return
     ----------
     dataframe
    '''
    return df[df[strColumn].notna()]


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


def filterByDfColContains(df, strColumn, strValue, blnCase=True):
    '''
    Filter a dataframe where a value is in the column.
    ...

     Parameters
     ----------
     df : dataframe 
     strColumn : str (dataframe column to filter by)
     strValue : string (value to filter by)
     blnCase : boolean (whether to search using case sensitivity or not; defaults to case sensitive)

     Return
     ----------
     dataframe

     Example
     ----------
     dfRow = filterByDfColContains(dfFileMd, 'cdmTableName', strTableName).reset_index() # `reset_index` makes sure the
     if "tableDescription" in dfRow:
        print("DESCRIPTION:",dfRow["tableDescription"][0])
    '''
    return df[df[strColumn].str.contains(strValue, case=blnCase)]


def readCsvStandard(strFilePath, intRows=None, blnUseAllColumns=True, vSep=','):
    '''
    This method ensures that when the CSV files are read, they are treated consistently.
    ...

     Parameters
     ----------
     strFilePath : string (path to the CSV file; NOTE: this should be the absolute path to the file)
     intRows : int (number of row we want returned for large datasets where we do not need all rows)

     Return
     ----------
     dataframe
    '''
    if blnUseAllColumns:
        return pd.read_csv(strFilePath, quoting=1, header=0, nrows=intRows, low_memory=False, sep=vSep).convert_dtypes().astype(pd.StringDtype()).fillna(".")  # we must convert EVERYTHING to strings since we assume the metadata categories (keys and values) will be cast to strings to ensure matches
        # `fillna(".")` adds `.` to empty cells; we need `.convert_dtypes()` to prevent ints from becoming floats and we need to do this BEFORE calling `astype("string") which ensures everything is treated as a string`
    else:   # we only want the first column of data for determining the number of rows in the data table
        return pd.read_csv(strFilePath, header=0, nrows=intRows, usecols=[0], sep=vSep)


def readSasDatatable(strFilePath):
    '''
    Simply reads a SAS file to a datatable
    ...

     Parameters
     ----------
     strFilePath : string (path to the CSV file; NOTE: this should be the absolute path to the file)
     intRows : int (number of row we want returned for large datasets where we do not need all rows)

     Return
     ----------
     dataframe
    '''
    df = pd.read_sas(strFilePath, encoding="utf-8").convert_dtypes()
    return df


def saveToCsv(strFilePath, df):
    '''
    Save a dataframe to a CSV file.

     Parameters
     ----------
     strFilePath : string (path to the CSV file; NOTE: this should be the absolute path to the file)
     df : dataframe (the dataframe we wish to save to a CSV file)

    '''
    df.to_csv(strFilePath, encoding='utf-8', index=False, quoting=1)


def getRowCount(strFilePath):
    '''
    This method is useful for very large CSV files were we simply wish to know the row count.

     Parameters
     ----------
     strFilePath : string (path to the CSV file; NOTE: this should be the absolute path to the file)

     Return
     ----------
     number of rows
    '''
    df = readCsvStandard(strFilePath, None, False)
    print("getting row count of (assuming the first line is a header)", len(df))
    return len(df)

    '''
    The following works, but may report more rows than exist.
    '''
    # import subprocess
    # num_lines = int(subprocess.check_output("wc -l "+strFilePath, shell=True).split()[0]) - 1
    # print("getting row count of (assuming the first line is a header)", num_lines)
    # return num_lines


def getValueCounts(df, strColumnName):
    '''
    For a dataframe, count the records for each unique value in a column.

     Parameters
     ----------
     strColumnName : string (name of the column in the dataframe where we want to know the record counts of each unique value)
     df : dataframe (the dataframe we wish to search)

     Returns
     ----------
     A dataframe showing the counts for each value in a column.
    '''
    return df[strColumnName].value_counts()


# @title Replace the categorical numeric data with the string categories in a dataframe
def dfMapCategories(df):
    '''
    [incomplete] Need to create code to map categories/labels to int values.
    
    '''
    return "need to create code to map categories"
    # dictMetadata = self.getFileMetadata(strFileName)
    # for colname in list(df.columns):  # for each data file variable/column
    #     file_index = next((index for (index, obj) in enumerate(dictMetadata['variables']) if colname in obj['name']), "None") # we need to know the index of the variable within the dictMetadata object
    #     if (file_index!="None" and dictMetadata['variables'][file_index]['value']['format']=='categorical'): # if a variable contains categorical values
    #         jsonVL = json.dumps(dictMetadata['variables'][file_index]['value']['category'])  # convert the categories to json
    #         intVL = json.loads(jsonVL, object_hook=self.keysToInt)  # replace string keys with integer so we can map the json
    #         df[colname] = df[colname].map(intVL)  # map the categories to the columns
    # return df