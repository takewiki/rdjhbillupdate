#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    reshapedata LLC
"""
import platform
from setuptools import setup
from setuptools import find_packages

setup(
    name='rdjhbillupdate',
    version='1.2.8',
    install_requires=[
        'requests',
    ],
    packages=find_packages(),
    license='Apache License',
    author='zhangchaoyang',
    author_email='764563896@qq.com',
    url='http://www.reshapedata.com',
    description='reshape data type in py language ',
    keywords=['reshapedata', 'rdt', 'pyrdt'],
    python_requires='>=3.6',
)


# python setup.py bdist_wheel