# Upgrade pip
python -m pip install --upgrade pip

# Install package
pip install virtualenv

# Create venv right into project folder 
virtualenv ./my_env

# Load and activate virtual environment 
. my_env/bin/activate

# Test environment
pip list

# Exit virtual environment
deactivate

# Repo ignore 
echo 'my_env/' > .gitignore

: '
Package    Version
---------- -------
pip        22.3.1
setuptools 65.6.3
wheel      0.38.4
'