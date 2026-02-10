'''
We simply use this script to test that all required Python packages are included in our requirements.txt file.
This file imports all of the scripts include in this package.
We run the `make testVenv` command to call this script. If any packages are missing from
our requirements.txt file then we will be alerted. Any missing packages need to be added
to the `installRequirements` make command.
'''
from py_datacuration._datatable import *
from py_datacuration._display import *
from py_datacuration._encoding import *
from py_datacuration._export import *
from py_datacuration._file import *
from py_datacuration._json import *
from py_datacuration._model import *
from py_datacuration._mysql_db import *
from py_datacuration._nb import *
from py_datacuration._pyth import *
from py_datacuration.DatasetModel import *

print("Testing complete")