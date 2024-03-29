# windlass
A place for me to experiment with the EAGLE and DALiuGE in peace and tranquility.

Intended to be cloned alongside my own DAliuGE fork. For all intents and purposes this repository contains development
notes for that reprository as well. 

## Setup
If you are on a ubuntu machine refer to setup.sh for instructions.
I recommend creating a conda environment first. 
If you do not make sure uwsgi is installed in your current python environment and comment out line 14 of setup.sh

## Miscellaneous Setup Gripes
- Need to change EAGLE config.py line 14 to `DEFAULT_TRANSLATOR_URL = 'http://localhost:8084/gen_pgt'`

## Current Progress / Notes
An overview of what is here
- Experiments (branch: Experiment1)
  - Where I will formally maintain demonstrations of reproducibility 
- helloWorldExample 
  - Contains several example graphs and python scripts with the goal of producing a full introduction to reproducibility
  in DALiuGE
  - The major writeup is on Overleaf
  - A Jupyter notebook is in writing now (branch:helloworld)
- Rerun
  - Scratch notes and files used when developing the Rerun portion of code
- Repeat (branch: accumulateRepeat)
  - Scratch notes and files used to develop the Repeat portion of code
  - Significantly simpler since boilerplate is already present.
  - Importantly contains a specification of all fields for all supported DROP types
- ReproForwarding (branch: ReproForwarding)
  - In addition to signalling back to the node manager when reproducibility data is processed each DROP listens to its
  producers for the same reproducibility message
  - The callback is currently empty but is implemented in the base DROP class
  - Needs testing 
- Currently developing example codes for explanatory purposes
- Developing a systematic method to test Rerunning between two workflows

# Windlass - Formal Readme
## System Requirements
- OS: POSIX compliant Unix based system (Mac OS or Linux)
   - Ubuntu 18.04
   - Windows10 + WSL (Ubuntu 18.04)
- CPU: 
   - Modern architecture (x86)
- Memory:
   - 4GB+
- Storage:
    - 26MB
### Software Dependencies
- Python 3.6+
- DALiuGE 1.0+
- Merklelib 1.0
- Jupyter Notebook
### Tested Versions
### Hardware Requirements
No specialised hardware is required for execution of this software.
## Installation Guide
- In a Python environment of your choice (system, conda or virtual environment)
To simply use Windlass alone
- `pip install windlass` which should also install all necessary dependencies
Or for development
- `git clone https://github.com/pritchardn/windlass`
- `pip install -e windlass`
### Typical Install Time
- < 10 mins
## Demo
- In a unix terminal with your activated python environment
- Start a DALiuGE daemon (with verbose logging for reference)
  - `$ dlg daemon  -v -v -v -mm`
- In a separate terminal window in the same activated python environment
  - `$ python Experiments\EX1HelloWorld\EX1Driver.py` to run a series of example workflows
### Expected Output
- See Experiments\EX1HelloWorld\expected.csv for expected outputs
- The file your execution generated (Experiments\EX1HelloWorld\out.csv) should be identical in contents
### Expected Runtime
- Since eight workflows are run start to finish execution should take around three minutes
## Instructions for Use
### Reproduction Instructions