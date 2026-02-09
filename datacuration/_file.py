import hashlib, os

'''
This module contains file related functions.
'''
def findFile(filename, root_dir):
    """
    For a given file and root directory, find the subdirectory where the file lives.

     Parameters
     ----------
     filename : str "name of file to search"
     root_dir : str "The directory to locate the file within."

     Returns
     ----------
     String or False
     
     Example
     ----------
     fileExists = find_file(strRawDataFile, strDatasetPath)
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if filename in filenames:
            return dirpath
    return False


def listDirContents(root_dir):
    """
    For a given directory, return a list of all contents (files and directories), not subdirectories.

     Parameters
     ----------
     root_dir : str "The directory to search."

     Returns
     ----------
     List of directories and files
     
     Example
     ----------
     objDsMetadataTemp[strDataset]={"lstColumns":[*dfTableData], "files":listFiles(.strDatasetPath+"/"+strDataset), "tableName": objTable["TABLE_NAME"]}
    """
    return os.listdir(root_dir)


def isDirectory(strPath):
    """
    Simply checks if a path is a directory.

     Parameters
     ----------
     strPath : str "The path to search."

     Returns
     ----------
     Boolean
     
    """
    return os.path.isdir(strPath)


def isFile(strPath):
    """
    Simply checks if a path is a file.

     Parameters
     ----------
     strPath : str "The path to search."

     Returns
     ----------
     Boolean
     
    """
    return os.path.isfile(strPath)


def getModuleFuncsFromPath(strDir, strPackage, lstFileExclude=[]):
    """
    For a given directory, return a list of all Python functions and the files that contain them.

     Parameters
     ----------
     strDir : str "The file directory to search."
     strPackage : str "The name of the package we are restricting the search."
     lstFileExclude : list "Names of files to exclude"

     Returns
     ----------
     Markdown string
     
    """
    strReturn=""
    # print("searching",strPackage)
    import inspect
    import importlib.util
    from inspect import getmembers, getdoc, isfunction #, ismethod, isfunction, isclass
    for name in os.listdir(strDir):
        if isFile(os.path.join(strDir,name)) and "py" in name and name not in lstFileExclude:
            strReturn+="# "+name+"\n"  # prints the file containing functions
            script_name = os.path.basename(name).removesuffix(".py")  # do not use rstrip because it treats `_display.py` incorrectly
            # print(f"this is the script name {os.path.basename(name)} and {script_name}")
            # strReturn+="# ("+script_name+")\n"
            # print("."+script_name, strPackage)
            # Import it from its path so that you can use it as a Python object.
            try:
                p = importlib.import_module("."+script_name, package=strPackage)
                allMembers = getmembers(p)
                for strName, objMem in allMembers:
                    # print(m[1])
                    if hasattr(objMem, '__module__') and strPackage in objMem.__module__:
                        # print(m[1].__module__, m[0])
                        if hasattr(objMem, '__class__'):  # if the member is a class
                            # strReturn+="# ("+strName+")\n"
                            cm=getmembers(objMem,isfunction)  # get functions of the class
                            if cm:
                                for strNameC, objMemC in cm:
                                    strReturn+="> ## "+str(strName)+"."+str(strNameC)+"()\n"
                                    strReturn+="```\n"+str(getdoc(objMemC))+"\n```\n"
                            else:
                                strReturn+="> ## "+str(strName)+"()\n"  # this prints the function name
                                strReturn+="```\n"+str(getdoc(objMem))+"\n```\n"  # this prints the documentation following
            except Exception as e:
                print(f":::::::::::::::An error occurred: {e} for {script_name}")        
    return strReturn


def getSha2Hash(strFilePath):
    """
    Generates an SHA2 hash for a given file (used to check against files being uploaded to prevent duplicate file uploads).

     Parameters
     ----------
     strFilePath : str "The file path."

     Returns
     ----------
     SHA2 hash
    """
    hash = hashlib.sha256()
    with open(strFilePath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()


def getMd5Hash(strFilePath):
    """
    Generates an MD5 hash for a given file (used to check against files being uploaded to prevent duplicate file uploads).

     Parameters
     ----------
     strFilePath : str "The file path."

     Returns
     ----------
     MD5 hash
     
    """
    hash_md5 = hashlib.md5()
    with open(strFilePath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()