import os
import time

from dlg.apps.mpi import MPIApp
from dlg.ddap_protocol import DROPStates

output_fname = os.getcwd() + './mpi_result.out'

# Initialize our Drops
a = MPIApp('a', 'a', command='cpi.py', maxprocs=4, use_wrapper=False, args=['1000000'])
# Link Drops together

# Execute and wait (HACK)
a.async_execute()
time.sleep(5)
a.setCompleted()
# Inspect Results
for drop in ([a]):
    print(drop)
    print(drop.status)
    print(drop.status == DROPStates.COMPLETED)
