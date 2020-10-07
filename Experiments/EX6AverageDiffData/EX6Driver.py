# (c) Nicholas Pritchard 2020
# A preliminary Python script to actually test reproducibility between two DALiuGE Workflows
# Ensure a DALiuGE Master Manager is running on port 9000
# Ensure a DALiuGE Daemon is running on port 8000

import os
import sys

from Experiments.tools.labTools import full_trial_single

if __name__ == "__main__":
    arg = int(sys.argv[1])
    if arg == 0:
        print("Currently unsupported")  # full_trial('averageNumPySimple', 'averageMySimple', '../graphs/win/')
    else:
        full_trial_single('averageNumPySimple', '../graphs/ubuntu/', './ubu/')
        os.rename('../data/numbers1.in', '../data/numbers3.in')
        os.rename('../data/numbers2.in', '../data/numbers1.in')
        os.rename('../data/numbers3.in', '../data/numbers2.in')
        full_trial_single('averageNumPySimple', '../graphs/ubuntu/', './')
        os.rename('../data/numbers1.in', '../data/numbers3.in')
        os.rename('../data/numbers2.in', '../data/numbers1.in')
        os.rename('../data/numbers3.in', '../data/numbers2.in')
