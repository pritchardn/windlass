# (c) Nicholas Pritchard 2020
# A simple Python script to setup both an EAGLE and DALiuGE server

import pathlib
import subprocess
from sys import stdin, stdout, stderr
from dlg.common import tool
from dlg.restutils import RestClient, RestClientException


LGWEB_PORT = 8000
HOME = pathlib.Path(__file__).parent.absolute()
TEMP = HOME / "temp/"
LGFILES = HOME / "lgdir/"

print(HOME)
print(TEMP)
print(LGFILES)


# common.terminate_or_kill(self.web_proc, 10)
