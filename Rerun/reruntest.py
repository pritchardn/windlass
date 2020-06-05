# (c) Nicholas Pritchard 2020
# A simple Python script to setup both an EAGLE and DALiuGE server

import optparse
import pathlib

from dlg.translator.tool_commands import fill, dlg_unroll

HOME = pathlib.Path(__file__).parent.absolute()
TEMP = HOME / "temp/"
LGFILES = HOME / "lgdir/"

print(HOME)
print(TEMP)
print(LGFILES)

lgt = 'HelloWorld3.graph'
lg = 'HelloWorld3LG.graph'
pgt = 'HelloWorld3PGT.graph'
pg = 'HelloWorld3PG.graph'


parser = optparse.OptionParser()
fill(parser, ['-L', lgt, '-R', '1', '-o', lg, '-f', 'newline'])
parser = optparse.OptionParser()
dlg_unroll(parser, ['-L', lg, '-o', pgt, '-f', 'newline'])
# unroll = tool.start_process('unroll', [], stdin=fill.stdout, stdout=subprocess.PIPE)
# partition = tool.start_process('partition', stdin=unroll.stdout, stdout=subprocess.PIPE)
# map_ = tool.start_process('map', ['-N', '127.0.0.1,127.0.0.1'], stdin=partition.stdout, stdout=subprocess.PIPE)
# sub = tool.start_process('submit', ['-p', '8000', '-w'], stdin=map_.stdout, stdout=subprocess.PIPE)
# print(sub.communicate()[0])
