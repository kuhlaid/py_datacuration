'''
This module contains functions that pertain to Notebook display.
'''
from IPython.display import HTML, Markdown, display, clear_output
import pandas as pd
from pandas import DataFrame

def ClearOutput(strNotice=""):
    '''
    Run this function to 'reset' any code output and replace it with the `strNotice` value.

     Parameters
     ----------
     strNotice : string (Any string such as "Your configuration is complete" to use for replacing code output.)

     Example
     ----------
     ClearOutput("This string will replace the last output of the cell")
    '''
    clear_output(wait=True)
    print(strNotice)


def showTable(dictObj, lstHeader=[], lstSort=[], lstColRename=[], displayType="Markdown", blnAscending=False):
    '''
    This transforms a dictionary to a dataframe, applies column renaming, sorts the colums, and outputs a table based on the colums specified.

     Parameters
     ----------
     dictObj : dict (A JSON object of properties of arrays)
     lstHeader : list (A list of the renamed columns for headers)
     lstSort : list (A list of the renamed columns to sort by)
     lstColRename : list (A list of dictionaries of original column name and their replacement)

     Example
     ----------
     showTable({"name":[], "desc":[], "fmt": []},
     ["Notebook", "Description", "Format"], 
     ["Notebook"], 
     [{"name": "Notebook"},{"desc": "Description"},{"fmt": "Format"}])
    '''
    dfFileList = pd.DataFrame(dictObj)   # assign the list to a dataframe for sorting and display
    if len(lstColRename)>0:
        for item in lstColRename:
            dfFileList.rename(columns=item, inplace = True)
    if displayType=="Markdown":
        display(Markdown(dfFileList[lstHeader].sort_values(by=lstSort, ascending=blnAscending).to_markdown()))
    else:
        display(HTML(dfFileList[lstHeader].sort_values(by=lstSort, ascending=blnAscending).to_html()))


def toMarkdown(strValue):
    """
    Render a Markdown string.

     Parameters
     ----------
     strValue : str "Markdown syntax to render."
     
     Example
     ----------
     toMarkdown("# This is a header")
    """
    display(Markdown(strValue))