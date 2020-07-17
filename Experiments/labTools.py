import json
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


def test_identical(w1: str, w2: str):
    f1 = open(w1 + '.out')
    f2 = open(w2 + '.out')
    r1 = json.load(f1)
    r2 = json.load(f2)
    f1.close()
    f2.close()

    return set(r1['reprodata']['leaves']) == set(r2['reprodata']['leaves'])


def summarise_run(record: dict):
    return {'result_hash': record['reprodata']['leaves'], 'meta_data': record['reprodata']['meta_data'],
            'meta_merkleroot': record['reprodata']['merkleroot']}
