import os
import time

from dlg.apps.archiving import NgasArchivingApp
from dlg.apps.bash_shell_app import BashShellApp
from dlg.ddap_protocol import DROPStates
from dlg.drop import FileDROP
from dlg.droputils import allDropContents

output_fname = os.getcwd() + '/result5.out'
input_fname = os.getcwd() + '/input.in'

# Initialize our drops
a = FileDROP('a', 'a', filepath=input_fname)
b = BashShellApp('b', 'b', command="echo Hello $(cat %i0) > %o0")
c = FileDROP('c', 'c', filepath=output_fname)
d = NgasArchivingApp('d', 'd')
# Link drops together
b.addInput(a)
b.addOutput(c)
d.addInput(c)

# Execute and wait
a.setCompleted()
time.sleep(5)

# Inspect results
for drop in (a, b, c, d):
    print(drop)
    print(drop.status)
    print(drop.status == DROPStates.COMPLETED)

# Check files are written correctly
print(allDropContents(c))
