# (c) Nicholas Pritchard 2020
# A simple Python script to setup both an EAGLE and DALiuGE server

import pathlib
import subprocess
from dlg.common import tool

LGWEB_PORT = 8000
HOME = pathlib.Path(__file__).parent.absolute()
TEMP = HOME / "temp/"
LGFILES = HOME / "lgdir/"

print(HOME)
print(TEMP)
print(LGFILES)

lg = 'HelloWorld3.graph'

fill = tool.start_process('fill', ['-L', lg], stdout=subprocess.PIPE)
unroll = tool.start_process('unroll', [], stdin=fill.stdout, stdout=subprocess.PIPE)
partition = tool.start_process('partition', stdin=unroll.stdout, stdout=subprocess.PIPE)
map_ = tool.start_process('map', ['-N', '127.0.0.1,127.0.0.1'], stdin=partition.stdout, stdout=subprocess.PIPE)
sub = tool.start_process('submit', ['-p', '8000', '-w'], stdin=map_.stdout, stdout=subprocess.PIPE)
print(sub.communicate()[0])
