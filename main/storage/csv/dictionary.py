"""CSV Dict:
It is often more convenient to work with ...
DictReader and DictWriter objects.
You can pass headers values as arguments.
"""
import csv, pathlib
from typing import AnyStr
DIR = pathlib.Path(__file__).resolve().parent

# Dictionary Reader
with open(DIR / 'data/fileH1.csv') as file:
    dr = csv.DictReader(file)
    for row in dr:
        print(row['A'], row['B'], row['C'])
            # 11 12 13
            # 21 22 23
            # 31 32 33

# Dictionary Writer
with open(DIR / 'data/fileH2.csv', 'w', newline='') as file:
    dw = csv.DictWriter(file, ['A', 'B', 'C'])
    dw.writeheader()
    dw.writerow({'A':11, 'B':12, 'C':13})
    dw.writerow({'A':21, 'B':22, 'C':23})
    dw.writerow({'A':31, 'B':32, 'C':33})

# Check the file
A = []
with open(DIR / 'data/fileH2.csv') as file:
    dr = csv.DictReader(file)
    for row in dr:
        A.append(row['A'])
print(A)
    # ['11', '21', '31']