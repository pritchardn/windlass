# windlass
A place for me to experiment with the EAGLE and DALiuGE in peace and tranquility.

## Setup
If you are on a ubuntu machine refer to setup.sh for instructions.
I recommend creating a conda environment first. 
If you do not make sure uwsgi is installed in your current python environment and comment out line 14 of setup.sh

## Miscellaneous Setup Gripes
- Need to change EAGLE config.py line 14 to `DEFAULT_TRANSLATOR_URL = 'http://localhost:8084/gen_pgt'`

## Current Progress / Notes
- Currently developing example codes for explanatory purposes
- Also looking at implementing workflow rerunning (using a DALiuGE Fork)
