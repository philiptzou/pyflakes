#!/usr/bin/env python
# Copyright 2005-2011 Divmod, Inc.
# Copyright 2013 Florent Xicluna.  See LICENSE file for details
from __future__ import with_statement

import os.path
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    extra = {'scripts': ["bin/pyflakes"]}
else:
    if sys.version_info < (3,):
        extra = {'tests_require': ['unittest2'],
                 'test_suite': 'unittest2.collector'}
    else:
        extra = {'tests_require': ['unittest2py3k'],
                 'test_suite': 'unittest2.collector.collector'}
    extra['entry_points'] = {
        'console_scripts': ['pyflakes = pyflakes.api:main'],
    }


def get_version(fname=os.path.join('pyflakes', '__init__.py')):
    with open(fname) as f:
        for line in f:
            if line.startswith('__version__'):
                return eval(line.split('=')[-1])


def get_long_description():
    descr = []
    for fname in ('README.rst',):
        with open(fname) as f:
            descr.append(f.read())
    return '\n\n'.join(descr)


setup(
    name="pyflakes",
    license="MIT",
    version=get_version(),
    description="passive checker of Python programs",
    long_description=get_long_description(),
    author="Phil Frost",
    author_email="indigo@bitglue.com",
    maintainer="Florent Xicluna",
    maintainer_email="pyflakes-dev@lists.launchpad.net",
    url="https://launchpad.net/pyflakes",
    packages=["pyflakes", "pyflakes.scripts", "pyflakes.test"],
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    **extra)
