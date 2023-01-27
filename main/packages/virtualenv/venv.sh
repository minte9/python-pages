python -m pip install --upgrade pip
pip install virtualenv


# Create
virtualenv ./my_env

# Activate
. my_env/bin/activate

# Test
pip list                

: '
Package    Version
---------- -------
pip        22.3.1
setuptools 65.6.3
wheel      0.38.4
'

# Exit
deactivate              


echo 'my_env/' > .gitignore