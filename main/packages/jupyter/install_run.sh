virtualenv ./notebook     # create env
. notebook/bin/activate   # load and activate

pip install jupyter       # install
pip install matplotlib
pip install pandas

echo 'notebook/' > .gitignore
echo '.ipynb_checkpoints/' >> .gitignore

jupyter notebook          # run