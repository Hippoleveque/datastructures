#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='sample',
    version='0.1.0',
    description='most classical datastructures in python',
    author='Hippolyte Lévêque',
    author_email='hippolyte.leveque@gmail.com',
    packages=find_packages(exclude=('tests'))
)
