import os
import pickle
import time

from dlg.apps.pyfunc import PyFuncApp
from dlg.ddap_protocol import DROPStates
from dlg.drop import FileDROP, InMemoryDROP
from dlg.droputils import allDropContents

output_fname = os.getcwd() + '/result6.out'


def hello_world(s='Everybody'):
    return "Hello " + s


fname = 'helloWorldExample.dropbased.helloS_python.hello_world'

# Initialize our Drops
a = InMemoryDROP('a', 'a')
b = PyFuncApp('b', 'b', func_name=fname)
c = FileDROP('c', 'c', filepath=output_fname)

# Link Drops together
b.addInput(a)
b.addOutput(c)

# Execute and wait (HACK)
a.write(pickle.dumps("World"))
a.setCompleted()
time.sleep(5)

# Inspect Results
for drop in (a, b, c):
    print(drop)
    print(drop.status)
    print(drop.status == DROPStates.COMPLETED)

# Check the file was written correctly
print(pickle.loads(allDropContents(c)))
