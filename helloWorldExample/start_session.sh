#!/bin/bash

HOME=$(pwd)
TEMP="$HOME""/temp"
LGDIR="$HOME""/lgdir"

dlg lgweb -d "$LGDIR" -t "$TEMP" -H "localhost"
