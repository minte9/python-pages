"""Read config.ini file:
"""
import configparser, pathlib
DIR = pathlib.Path(__file__).resolve().parent

config = configparser.ConfigParser()
config.read(DIR/'config.ini')

HOME_UNIX = config['HOME']['UNIX']
HOME_WINDOWS = config['HOME']['WINDOWS']
M9_URLs = config['M9']['URLS'].split(',')
DEBUG = config['APP']['DEBUG']

assert HOME_UNIX == '/home/catalin'                         # pass
assert DEBUG == 'False'                                     # pass
assert M9_URLs[1].strip() == 'https://www.minte9.com/java'  # pass