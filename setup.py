#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import sys

from setuptools import setup, find_packages


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()

setup(
    name='latexrender',
    version='0.3.2',
    description='A simple Flask app for rendering latex snippets into images.',
    long_description=readme,
    author='Luke Pomfrey',
    author_email='lpomfrey@gmail.com',
    url='https://github.com/lpomfrey/latexrender',
    packages=find_packages(exclude='tests'),
    package_dir={'latexrender': 'latexrender'},
    include_package_data=True,
    install_requires=[
        'flask',
        'pillow',
    ],
    license="BSD",
    zip_safe=False,
    keywords='latexrender',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=[
        'webtest',
    ],
)
