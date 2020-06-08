import os
import pickle
import time

from dlg.apps.pyfunc import PyFuncApp
from dlg.ddap_protocol import DROPStates
from dlg.drop import FileDROP
from dlg.droputils import allDropContents

output_fname = os.getcwd() + '/result6.out'


def hello_world():
    return "Hello World"


fname = 'helloWorldExample.dropbased.helloWorld_python.hello_world'

# Initialize our Drops
a = PyFuncApp('a', 'a', func_name=fname)
b = FileDROP('b', 'b', filepath=output_fname)

# Link Drops together
a.addOutput(b)

# Execute and wait (HACK)
a.async_execute()
time.sleep(5)

# Inspect Results
for drop in (a, b):
    print(drop)
    print(drop.status)
    print(drop.status == DROPStates.COMPLETED)

# Check the file was written correctly
print(pickle.loads(allDropContents(b)))
