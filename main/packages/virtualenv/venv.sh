python -m pip install --upgrade pip
pip install virtualenv

virtualenv ./my_env     # create

. my_env/bin/activate   # load and activate
pip list                # test env     
deactivate              # exit env

source my_env/bin/activate # second method
pip list
deactivate

: '
Package    Version
---------- -------
pip        22.3.1
setuptools 65.6.3
wheel      0.38.4
'
        
echo 'my_env/' > .gitignore