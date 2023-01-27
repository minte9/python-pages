virtualenv ./notebook     # create env
. notebook/bin/activate   # load and activate

pip install jupyter       # install
pip install matplotlib

echo 'notebook/' > .gitignore
echo '.ipynb_checkpoints/' >> .gitignore

jupyter notebook          # run