#!/usr/bin/env python
"""The setup file for installing Skelator as a module"""
import os
from setuptools import setup, find_packages

setup(
    version="0.11.0",
    setup_requires=[],
    test_require=[],
    package_data={'skelator': ['assets/*']},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'skelator = skelator.main:cli_interface',
            'skelator2 = skelator.also_main:cli_interface'
        ]
    }
)
