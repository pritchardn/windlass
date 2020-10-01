# (c) Nicholas Pritchard 2020
# A preliminary Python script to actually test reproducibility between two DALiuGE Workflows
# Ensure a DALiuGE Master Manager is running on port 9000
# Ensure a DALiuGE Daemon is running on port 8000

import sys

from Experiments.tools.labTools import full_trial

if __name__ == "__main__":
    arg = int(sys.argv[1])
    if arg == 0:
        print("Currently unsupported")  # full_trial('averageNumPySimple', 'averageMySimple', '../graphs/win/')
    else:
        full_trial('averageNumPySimple', 'averageMySimple', '../graphs/ubuntu/', './ubu/')
