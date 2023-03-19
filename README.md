# Docs.py
### A basic Python Class for generating API documentation as a PDF.

## Notes
Tested on Fedora 37

## Requirements
- [x] Python 3.8
- [x] python3-pip
- [x] conda
- [ ] python3-virtualenv

## Installation
1. Install python3, python3-pip and anaconda. Anaconda can be retrieved from [here](https://www.anaconda.com/products/individual). If you are on Windows, you can install anaconda with [chocolatey](https://chocolatey.org/) using `choco install anaconda3`.
2. Create a conda environment with `conda create --name DocsPy python=3.8`.
3. Activate the conda environment with `conda activate DocsPy`.
4. Install the requirements with `python3 -m pip install -r requirements.txt`.

## Usage (Setup)
0. Download this project with `git clone https://github.com/PhysCorp/DocsPy.git`
1. Activate the conda environment with `conda activate DocsPy`.
2. Edit the `docs.py` file to your liking with proper documentation for each argument.
3. Run `python3 docs.py` with the name of a python file as an argument. For example, `python3 docs.py name="test.py"`.

## Usage (Production)
1. Run `python3 docs.py` with the name of a python file as an argument. For example, `python3 docs.py name="test.py"`.

### Alternate Instructions using virtualenv
Create a new virtualenv with `python3 -m venv venv`.
Activate the virtualenv with `source venv/bin/activate`.
Install the requirements with `python3 -m pip install -r requirements.txt`.

## Uninstall
1. Deactivate the conda environment with `conda deactivate`.
2. Remove the conda environment with `conda remove --name DocsPy --all`.