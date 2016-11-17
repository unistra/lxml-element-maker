#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

with open('README.rst') as readme:
    long_description = readme.read()

with open('requirements.txt') as requirements:
    lines = requirements.readlines()
    libraries = [lib for lib in lines if not lib.startswith('-')]
    dependency_links = [link.split()[1] for link in lines if
                        link.startswith('-f')]

setup(
    name='lxml-element-maker',
    version='1.0.0',
    author='di-dip-unistra',
    author_email='di-dip@unistra.fr',
    maintainer='di-dip-unistra',
    maintainer_email='di-dip@unistra.fr',
    url='https://github.com/unistra/lxml-element-maker',
    license='PSF',
    description='Transform a python structure to an xml element with lxml',
    long_description=long_description,
    packages=find_packages(),
    download_url='http://pypi.python.org/pypi/lxml-element-maker',
    install_requires=libraries,
    dependency_links=dependency_links,
    keywords=['lxml', 'python', 'maker', 'xml', 'element'],
    entry_points={},
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4'
    )
)
