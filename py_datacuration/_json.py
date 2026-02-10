'''
This module contains functions that pertain to working with JSON files and data.
'''
import json
import numpy as np

def validJson(strFilePath, blnReturn=False):
    '''
    Ensure we are working with a valid JSON file or our JSON file has not corrupted.

     Parameters
     ----------
     strFilePath : string (path to the file)
     blnReturn : boolean (whether we want to return the JSON object after validation passes)

     Returns
     ----------
     Dict

     Example
     ----------
     self._config = validJson("strPathTo/something.json", True)
    '''
    f = open(strFilePath, "r")
    try:
        objJson = json.loads(f.read()) # put JSON-data to a variable
        f.close()
        if blnReturn:
            return objJson
    except json.decoder.JSONDecodeError:
        raise RuntimeError("***ERROR: Invalid JSON for "+strFilePath+"***")


def getNestedElement(data, strKeys):
    '''
    This searches a data object (JSON) for nested properties based on a simple `dot-separated` string that can be dynamically generated and allows for accessing properties dynamically.
    
     Parameters
     ----------
     data : object/dict
     strKeys : string (format like 'a.b.c' where each property in the tree is separated by a `.`)

     Returns
     ----------
     Dict
     
     Example
     ----------
     lstNotebook["desc"].append(getNestedElement(objNotebook,"metadata._cc__AboutThisNotebook_"))
    '''
    if isinstance(strKeys, str):
        strKeys = strKeys.split('.')
    temp = data
    for key in strKeys:
        try:
            temp = temp[key]
        except (TypeError, KeyError):
            return None
    return temp


    
# def setNestedElement(dic, keys, value, create_missing=True):
#     '''
#     This sets a data object element. Takes keys in a format like 'a.b.c' to more easily set nested dict/object properties dynamically.
    
#      Parameters
#      ----------
#      dic : object/dict
#      keys : list (format like `['person', 'address', 'city']` where each property in the tree is separate string in the list and ordered)
#      value : varies
#      create_missing : boolean (defines a missing element should be created or not)
#     '''
#     d = dic
#     for key in keys[:-1]:
#         if key in d:
#             d = d[key]
#         elif create_missing:
#             d = d.setdefault(key, {})
#         else:
#             return dic
#     if keys[-1] in d or create_missing:
#         d[keys[-1]] = value
#     return dic


def convertDictKeysToInt(input_dict):
    '''
    This converts key values to integer for a dictionary.
    NOTE: this function mainly used for applying categories to STATA data
    
     Parameters
     ----------
     input_dict : dict (JSON object to scan)

     Returns
     ----------
     Dict
    '''
    return {int(key): value for key, value in input_dict.items()}


def saveJson(obj, strFileOutPath):
    '''
    Save JSON object to a file (with auto formatting applied).
    
     Parameters
     ----------
     strFileOutPath : string (file path to output the JSON object)

     Example
     ----------
     saveJson(objMetadata, os.path.join(self._config["_cc__strOutputPath"],"gen."+self._config["metaDataFilename"]))
    '''
    with open(strFileOutPath, mode='w') as jsonFile:
        jsonFile.write(json.dumps(obj, indent=2, allow_nan=False, cls=NpEncoder))


class NpEncoder(json.JSONEncoder):
    '''
    This is important for correcting data to be converted to clean JSON using `json.dumps`. This is a callback object.
    
     Example
     ----------
     with open("gen.spectraSchema.deref.json", mode='w') as jsonFile:  # save the object to a file
            jsonFile.write(json.dumps(jsonDeref, indent=2, allow_nan=False, cls=NpEncoder))
    '''
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)