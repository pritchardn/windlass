from dlg.apps.bash_shell_app import StreamingOutputBashApp, StreamingInputBashApp
from dlg.ddap_protocol import DROPStates
from dlg.drop import FileDROP, InMemoryDROP
from dlg.droputils import allDropContents
import time
import os

output_fname = os.getcwd() + '/result3.out'

# Initialize our drops
a = StreamingOutputBashApp('a', 'a', command=r"echo -en 'world'")
b = InMemoryDROP('b', 'b')
c = StreamingInputBashApp('c', 'c', command="echo Hello $(cat) > %o0")
d = FileDROP('d', 'd', filename=output_fname)

# Link Drops together
a.addOutput(b)
c.addStreamingInput(b)
c.addOutput(d)

# Execute and wait (HACK)
a.async_execute()
time.sleep(7)

# Inspect Results
for drop in (a, b, c, d):
    print(drop)
    print(drop.status)
    print(drop.status == DROPStates.COMPLETED)

# Check the file was written correctly
print(allDropContents(d))
