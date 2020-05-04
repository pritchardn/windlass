#!/bin/bash

pip install daliuge

git clone https://github.com/ICRAR/EAGLE.git
cd EAGLE || exit
sudo apt install npm
sudo npm install -g typescript
conda install -c conda-forge uwsgi # Remove if not using conda
pip install .
cd ..