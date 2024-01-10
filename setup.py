#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Installation and deployment script."""

import glob
import os
import sys

try:
  from setuptools import find_packages, setup
except ImportError:
  from distutils.core import find_packages, setup

from pip._internal.network.session import PipSession
from pip._internal.req.req_file import parse_requirements

# Change PYTHONPATH to include UnifiedLog so that we can get the version.
sys.path.insert(0, '.')

import UnifiedLog  # pylint: disable=wrong-import-position


unifiedlog_description = (
    'A parser for Unified logging .tracev3 files.')

unifiedlog_long_description = (
    'A parser for Unified logging .tracev3 files.')

setup(
    name='UnifiedLog',
    version=UnifiedLog.__version__,
    description=unifiedlog_description,
    long_description=unifiedlog_long_description,
    license='MIT',
    url='https://github.com/ydkhatri/UnifiedLogReader',
    maintainer='Yogesh Khatri',
    maintainer_email='yogesh@swiftforensics.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
    packages=find_packages('.', exclude=[
        'tests', 'tests.*']),
    package_dir={
        'UnifiedLog': 'UnifiedLog'
    },
    scripts=glob.glob(os.path.join('scripts', '[A-Za-z]*.py')),
    data_files=[
        ('share/doc/UnifiedLog', [
            'LICENSE.txt', 'README.md']),
    ],
    install_requires=[req.requirement for req in parse_requirements(
        'requirements.txt', session=PipSession(),
    )],
)
