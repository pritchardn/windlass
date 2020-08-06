# (c) Nicholas Pritchard 2020
# A simple Python script to setup both an EAGLE and DALiuGE server

import optparse
import pathlib

from dlg.translator.tool_commands import dlg_fill, dlg_unroll, dlg_partition, dlg_map, dlg_submit

HOME = pathlib.Path(__file__).parent.absolute()
TEMP = HOME / "temp/"
LGFILES = HOME / "lgdir/"

print(HOME)
print(TEMP)
print(LGFILES)

lgt = 'HelloWorld3.graph'
lg = 'HelloWorld3LG.graph'
pgt = 'HelloWorld3PGT.graph'
pgs = 'HelloWorld3PGS.graph'
pg = 'HelloWorld3PG.graph'
rg = 'HelloWorld3PG_final.graph'

parser = optparse.OptionParser()
dlg_fill(parser, ['-L', lgt, '-R', '2', '-o', lg, '-f', 'newline'])
parser = optparse.OptionParser()
dlg_unroll(parser, ['-L', lg, '-o', pgt, '-f', 'newline'])
parser = optparse.OptionParser()
dlg_partition(parser, ['-P', pgt, '-o', pgs, '-f', 'newline'])
parser = optparse.OptionParser()
dlg_map(parser, ['-P', pgs, '-N', '127.0.0.1,127.0.0.1', '-o', pg, '-f', 'newline'])
parser = optparse.OptionParser()
dlg_submit(parser, ['-P', pg, '-p', '8000', '-R', '-o', rg, '-f', 'newline'])
