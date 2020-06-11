# (c) Nicholas Pritchard 2020
# A simple Python script to setup both an EAGLE and DALiuGE server

import optparse
import pathlib

from dlg.translator.tool_commands import dlg_fill, dlg_unroll, dlg_partition

HOME = pathlib.Path(__file__).parent.absolute()
TEMP = HOME / "temp/"
LGFILES = HOME / "lgdir/"

print(HOME)
print(TEMP)
print(LGFILES)

lgt = 'LinkExample.graph'
lg = 'LinkExampleLG.graph'
pgt = 'LinkExamplePGT.graph'
pgs = 'LinkExamplePGS.graph'
pg = 'LinkExamplePG.graph'


parser = optparse.OptionParser()
dlg_fill(parser, ['-L', lgt, '-R', '1', '-o', lg, '-f', 'newline'])
parser = optparse.OptionParser()
dlg_unroll(parser, ['-L', lg, '-o', pgt, '-f', 'newline'])
parser = optparse.OptionParser()
dlg_partition(parser, ['-P', pgt, '-o', pgs, '-f', 'newline'])
# map_ = tool.start_process('map', ['-N', '127.0.0.1,127.0.0.1'], stdin=partition.stdout, stdout=subprocess.PIPE)
# sub = tool.start_process('submit', ['-p', '8000', '-w'], stdin=map_.stdout, stdout=subprocess.PIPE)
# print(sub.communicate()[0])
