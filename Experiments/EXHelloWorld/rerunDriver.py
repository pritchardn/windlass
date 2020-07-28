# (c) Nicholas Pritchard 2020
# A preliminary Python script to actually test reproducibility between two DALiuGE Workflows
# Ensure a DALiuGE Master Manager is running on port 9000
# Ensure a DALiuGE Daemon is running on port 8000

from dlg.common.reproducibility.reproducibility import ReproducibilityFlags

from Experiments.tools.labTools import run_full_workflow, test_identical

if __name__ == "__main__":
    run_full_workflow("HelloSBash", ReproducibilityFlags.RERUN)
    run_full_workflow("HelloWorldBash", ReproducibilityFlags.RERUN)
    result = test_identical("HelloSBash", "HelloWorldBash")
    print(result)
