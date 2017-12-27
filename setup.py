from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import pysql

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='UTF-8') as f:
	long_description = f.read()

setup(
	name='PySQL',
	version=pysql.__version__,
	description='A MySQL implementation in Python',
	long_description=long_description,
	url='https://github.com/Adrian0350/PySQL',
	author='Adrián Zúñiga',
	author_email='jaime.ziga@gmail.com',
	platforms='any',
	keywords='mysql implementation development',  # Optional
	packages=['pysql'],
	tests_require=['pytest'],
	test_suite='pysql.test.test_pysql',
	include_package_data=True,
	classifiers=[
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: MIT License',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
	extras_require={
		'testing': ['pytest']
	}
)
