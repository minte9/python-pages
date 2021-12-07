"""Zip arhive
Compressing multiple files into a single archive file.
"""
import zipfile, os

DIR = os.path.dirname(os.path.realpath(__file__))

newZip = zipfile.ZipFile(DIR + '/data/archive.zip', 'w')
newZip.write(DIR + '/data/file1.txt', 'file1', compress_type=zipfile.ZIP_DEFLATED)
newZip.write(DIR + '/data/file2.txt', 'file2', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

archive = zipfile.ZipFile(DIR + '/data/archive.zip')
print(archive.namelist())
    # file1, file2

info = archive.getinfo('file1')
print(info.file_size) 
    # 3

archive.close()