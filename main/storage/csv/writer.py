"""CSV writer:
Use open() method and pass it 'w' argument.
On windows you'll also need to pass newline='' argument.
"""
import csv, pathlib
DIR = pathlib.Path(__file__).resolve().parent

# Writer
with open(DIR / 'data/file2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([11, 12, 13])
    writer.writerow([21, 22, 23])
    writer.writerow([31, 32, 33])

# Check
with open(DIR / 'data/file2.csv') as file:
    reader = csv.reader(file)
    data = list(reader)
    assert data[1][1] == '22'
    assert data[2][2] == '33'