# (c) Nicholas Pritchard 2020
# A simple Python script to setup both an EAGLE and DALiuGE server

import optparse
import pathlib

from dlg.translator.tool_commands import dlg_fill, dlg_unroll, dlg_partition, dlg_map

HOME = pathlib.Path(__file__).parent.absolute()
TEMP = HOME / "temp/"
LGFILES = HOME / "lgdir/"

print(HOME)
print(TEMP)
print(LGFILES)

lgt = 'mpitest.graph'
lg = 'mpitestLG.graph'
pgt = 'mpitestPGT.graph'
pgs = 'mpitestPGS.graph'
pg = 'mpitestPG.graph'

parser = optparse.OptionParser()
dlg_fill(parser, ['-L', lgt, '-R', '1', '-o', lg, '-f', 'newline'])
parser = optparse.OptionParser()
dlg_unroll(parser, ['-L', lg, '-o', pgt, '-f', 'newline'])
parser = optparse.OptionParser()
dlg_partition(parser, ['-P', pgt, '-o', pgs, '-f', 'newline'])
parser = optparse.OptionParser()
dlg_map(parser, ['-P', pgs, '-N', '127.0.0.1,127.0.0.1', '-o', pg, '-f', 'newline'])
parser = optparse.OptionParser()
# dlg_submit(parser, ['-P', pg, '-p', '8000', '-w'])