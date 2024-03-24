import os
import io
from pathlib import Path
from setuptools import setup

NAME = 'MLPackages'
DESCRIPTION = 'This is a simple loan prediction model.'
URL = 'https://github.com/fudge-fantastic'
EMAIL = 'adi.pandagle@gmail.com'
AUTHOR = 'Bluesalt'
REQUIRED_PYTHON = '>=3.9.0'

pwd = os.path.abspath(os.path.dirname(__file__))

# Get list of packages to install
def list_req(fname = 'requirements.txt'):
    with io.open(os.path.join(pwd, fname), encoding='utf-8') as f:
        return f.read().splitlines()
    
try:
    with io.open(os.path.join(pwd, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR
about = {}
with open(PACKAGE_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version

setup(

    name = NAME,
    version = about['__version__'],
    description = DESCRIPTION,
    long_description = long_description,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires = REQUIRED_PYTHON,
    url = URL,
    package_data= {'MLPackages' : ['VERSION.txt']},
    install_requires = list_req(),
    include_package_data= True,
    license='MIT'

)