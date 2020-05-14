import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyprofinet",
    version = "0.0.1",
    license="MIT",
    author = ("devkid (https://github.com/devkid/)", "Jonas Amstutz"),
    author_email = "jonasamstutz@gmail.com",
    description = ("Minimal Profinet implementation (DCP and ASYNC)"),
    packages=find_packages(),
    scripts=['bin/pyprofinet'],
    long_description=read('README.md'),
    install_requires=[])
