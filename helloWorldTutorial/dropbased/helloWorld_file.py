from dlg.apps.bash_shell_app import StreamingInputBashApp, StreamingOutputBashApp
from dlg.ddap_protocol import DROPStates
from dlg.drop import FileDROP, InMemoryDROP
from dlg.droputils import allDropContents
import time
import os


output_fname = os.getcwd() + '/result.out'

# Initialize our Drops
a = FileDROP('a', 'a', filepath=output_fname)

# Link Drops together

# Execute and wait (HACK)
a.write(b"Hello world")
a.setCompleted()

# Inspect Results
print(a)
print(a.status)
print(a.status == DROPStates.COMPLETED)

# Check the file was written correctly
print(allDropContents(a))
