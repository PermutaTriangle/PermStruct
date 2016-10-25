#!/usr/bin/env python
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
    packages=[
        'permstruct',
        'permstruct.dag',
        'permstruct.permutation_sets',
        'permstruct.permutation_sets.units',
        'permstruct.misc',
    ],
    long_description=read('README.md'),
    test_suite = 'tests'
)
