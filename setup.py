# -*- coding: utf-8 -*-
"""
Setup for RadSI - The Radiation Source Inventory
Author: Matthew Durbin
Date: Tue July 07 2020
"""

import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='RadSI',
    version='1.0.0',
    author='Matthew Durbin',
    author_email='mud370@psu.edu'
    description='A command-line interface radiation source inventory',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages()
    install_requires=[
        'setuptools',
        'pandas >= 1.0.3',
        'numpy >= 1.18.1',
        'fire >= 0.3.1',
        'matplotlib >= 3.1.3'
    ],
    python_requires='>=3.5'
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/matthewdurbin/RadSI'
)