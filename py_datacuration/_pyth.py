'''
This module contains functions related to working with a Python file.
'''
import inspect
from datetime import datetime
from zoneinfo import ZoneInfo

def getClassMethods(cls):
    """
    List the methods found within a class.

     Parameters
     ----------
     cls : class object "e.g. if we passed in Worker, it would analyze the methods within the Worker class"

     Returns
     ----------
     List
     
     Example
     ----------
     method_list = getClassMethods(Worker)
    """
    methods = inspect.getmembers(cls, predicate=inspect.isroutine)
    return [name for name, _ in methods if not name.startswith("__")]


def getDateTime(strFormat='', strFromTimestamp=''):
    """
    Return the current date/time (EST) or returns a date/time from a timestamp using a format we choose.

     Parameters
     ----------
     strFormat : string "strftime() formatted string"
     strFromTimestamp :  string "timestamp to format"

     Returns
     ----------
     String

     Example
     ----------
     getDateTime('%Y-%m-%d')  # returns on year-month-day
    """
    if strFromTimestamp=='':
        utc_now = datetime.now(ZoneInfo("UTC"))
    else:
        utc_now = datetime.fromtimestamp(strFromTimestamp, tz=ZoneInfo("UTC"))
    
    
    if strFormat=="":
        return utc_now.astimezone(ZoneInfo("America/New_York"))
    else:
        return utc_now.astimezone(ZoneInfo("America/New_York")).strftime(strFormat)