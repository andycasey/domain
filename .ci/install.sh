#!/bin/bash -x
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh;
bash miniconda.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
hash -r
conda config --set always_yes yes --set changeps1 no
conda update -q conda
conda info -a
conda config --add channels conda-forge
conda update --all
conda install --yes python=$TRAVIS_PYTHON_VERSION nose coverage coveralls
python setup.py install
