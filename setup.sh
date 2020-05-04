#!/bin/bash

git clone https://github.com/ICRAR/daliuge.git
cd daliuge || exit
pip install -e daliuge-common
pip install -e daliuge-translator
pip install -e daliuge-runtime
cd ..

git clone https://github.com/ICRAR/EAGLE.git
cd EAGLE || exit
sudo apt install npm
sudo npm install -g typescript
conda install -c conda-forge uwsgi # Remove if not using conda
pip install .
cd ..