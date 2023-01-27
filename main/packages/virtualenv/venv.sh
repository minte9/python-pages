# Upgrade pip
python -m pip install --upgrade pip

# Install package
pip install virtualenv

# Create venv right into project folder 
virtualenv ./my_env

# Load and activate virtual environment
. my_env/bin/activate

# Run some commends
pip list

# Exit virtual environment
deactivate

# Repo ignore 
echo 'my_env/' > .gitignore