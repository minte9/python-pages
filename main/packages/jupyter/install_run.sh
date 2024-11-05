virtualenv ./notebook     # create env
. notebook/bin/activate   # load and activate

pip install jupyter       # packages
pip install pandas

echo 'notebook/' > .gitignore
echo '.ipynb_checkpoints/' >> .gitignore

jupyter notebook          # run