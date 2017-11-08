#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext
import re

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


long_description = '%s\n%s' % (
    read('README.rst'),
    re.sub(':obj:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
)

setup(
    name='scancode-toolkit-contrib',
    version='2.0.1',
    license='Apache-2.0 with ScanCode acknowledgment and CC0-1.0 and others',
    description='ScanCode contributions - candidate additions to ScanCode.',
    long_description=long_description,
    author='ScanCode',
    author_email='info@scancode.io',
    url='https://github.com/nexB/scancode-toolkit-contrib',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'License :: OSI Approved :: CC0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    keywords=[
        'license', 'filetype', 'urn', 'date', 'codec',
    ],
    install_requires=[
        # compiledcode and packagedcode
        'macholib >=1.7',
        'altgraph >=0.13',

        #scancode-toolkit
        'scancode-toolkit',
    ],

    extras_require={
        ':platform_system == "Windows"': ['lxml == 3.6.0'],
        ':platform_system == "Linux"': ['lxml == 3.6.4'],
        ':platform_system == "Darwin"': ['lxml == 3.6.4'],

    },
)
