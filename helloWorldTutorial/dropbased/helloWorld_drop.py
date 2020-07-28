import os
import time

from dlg.apps.bash_shell_app import StreamingInputBashApp, StreamingOutputBashApp
from dlg.ddap_protocol import DROPStates
from dlg.drop import FileDROP, InMemoryDROP
from dlg.droputils import allDropContents

output_fname = os.getcwd() + '/result.out'

# Initialize our Drops
a = StreamingOutputBashApp('a', 'a', command=r"echo -en 'Hello world'")
b = InMemoryDROP('b', 'b')
c = StreamingInputBashApp('c', 'c', command="cat > %o0")
d = FileDROP('d', 'd', filepath=output_fname)

# Link Drops together
a.addOutput(b)
c.addStreamingInput(b)
c.addOutput(d)

# Execute and wait (HACK)
a.async_execute()
time.sleep(5)

# Inspect Results
for drop in (a, b, c, d):
    print(drop)
    print(drop.status)
    print(drop.status == DROPStates.COMPLETED)

# Check the file was written correctly
print(allDropContents(d))
