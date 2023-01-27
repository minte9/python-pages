python -m pip install --upgrade pip # Upgrade pip
pip install virtualenv              # Install package

virtualenv ./my_env     # Create venv right into project folder 
. my_env/bin/activate   # Load and activate virtual environment 

pip list                # Test environment

: '
Package    Version
---------- -------
pip        22.3.1
setuptools 65.6.3
wheel      0.38.4
'
deactivate              # Exit virtual environment

echo 'my_env/' > .gitignore