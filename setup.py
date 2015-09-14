import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "permstruct",
    version = "0.0.1",
    author = "Henning Ulfarsson",
    author_email = "henningu@ru.is",
    description = "An implementation of the PermStruct algorithm.",
    license = "BSD-3",
    keywords = "permutations generating rules",
    url = "https://github.com/PermutaTriangle/PermStruct",
    packages=['permstruct', 'tests'],
    long_description=read('README.md'),
)
