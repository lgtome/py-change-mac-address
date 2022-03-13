from importlib.resources import path
import io
import os
from platform import python_revision
from setuptools import setup,find_packages

NAME = 'py-change-mac-address-naayaa-oops'
DESCRIPTION = 'Test py proj'
URL = 'https://github.com/NaaYaa-oops/py-change-mac-address'
EMAIL = 'seryikotenok232@gmail.com'
AUTHOR = 'NaaYaa-oops'
REQUIRES_PYTHON = '>=2.7.18'
VERSION = '0.1.0'

REQUIRED = []
EXTRAS = []

absolute_path = os.path.abspath(os.path.dirname(__file__))


try:
   with io.open(os.path.join(absolute_path, 'README.md'), encoding='utf-8') as f:
    long_description=f.read()
    for line in f:
     print(line)
except FileNotFoundError:
   print(FileNotFoundError)
  
setup(
  name=NAME,
  version=VERSION,
  author=AUTHOR,
  author_email=EMAIL,
  description=DESCRIPTION,
  url=URL,
  long_description=long_description,
  long_description_content_type="text/markdown",
  classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
  package_dir={"":'.'},
  packages=find_packages(where='.'),
  python_revision=REQUIRES_PYTHON
)
