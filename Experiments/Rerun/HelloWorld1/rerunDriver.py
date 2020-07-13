# (c) Nicholas Pritchard 2020
# A preliminary Python script to actually test reproducibility between two DALiuGE Workflows
# Ensure a DALiuGE Master Manager is running on port 9000
# Ensure a DALiuGE Daemon is running on port 8000

import optparse

from dlg.common.reproducibility.reproducibility import ReproduciblityFlags
from dlg.translator.tool_commands import dlg_fill, dlg_unroll, dlg_partition, dlg_map, dlg_submit


def run_full_workflow(workflow: str, rmode: ReproduciblityFlags):
    lgt = workflow + ".graph"
    lg = workflow + "LG.graph"
    pgs = workflow + "PGS.graph"
    pgt = workflow + "PGT.graph"
    pg = workflow + "PG.graph"
    rg = workflow + ".out"

    rmodes = str(rmode.value)

    parser = optparse.OptionParser()
    dlg_fill(parser, ['-L', lgt, '-R', rmodes, '-o', lg, '-f', 'newline'])
    parser = optparse.OptionParser()
    dlg_unroll(parser, ['-L', lg, '-o', pgs, '-f', 'newline'])
    parser = optparse.OptionParser()
    dlg_partition(parser, ['-P', pgs, '-o', pgt, '-f', 'newline'])
    parser = optparse.OptionParser()
    dlg_map(parser, ['-P', pgt, '-N', '127.0.0.1,127.0.0.1', '-o', pg, '-f', 'newline'])
    parser = optparse.OptionParser()
    dlg_submit(parser, ['-P', pg, '-p', '8000', '-R', '-o', rg, '-f', 'newline'])


def summarise_run(workflow: str):
    return {}


if __name__ == "__main__":
    #run_full_workflow("HelloSBash", ReproduciblityFlags.RERUN)
    run_full_workflow("HelloWorldBash", ReproduciblityFlags.RERUN)
    #summarise_run("HelloSBash")
    #summarise_run("HelloWorldBash")
