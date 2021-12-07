"""Extract from zip file.
Extract all files into the current directory.
"""
import zipfile, os
from pathlib import Path

DIR = Path(__file__).resolve().parent

with zipfile.ZipFile(DIR / 'data/archive.zip') as archive:
    archive.extractall(DIR / 'data/extracted')

for root, dirs, files in os.walk(DIR / 'data/extracted'):
    for name in files:
        print(name)
            # file1
            # file2
