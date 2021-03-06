from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import io
import codecs
import os
import sys

import package

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.md'), encoding='UTF-8') as f:
	long_description = f.read()

class PyTest(TestCommand):
	def finalize_options(self):
		TestCommand.finalize_options(self)
		self.test_args = []
		self.test_suite = True

	def run_tests(self):
		import pytest
		errcode = pytest.main(self.test_args)
		sys.exit(errcode)

setup(
	name='Python-Module-Structure',
	version=package.__version__,
	description='A MySQL implementation in Python',
	long_description=long_description,
	url='https://github.com/Adrian0350/Python-Module-Structure',
	author='Adrián Zúñiga',
	author_email='jaime.ziga@gmail.com',
	platforms='any',
	keywords='python module package basic example implementation development',  # Optional
	packages=[
		'package'
	],
	install_requires=[],
	tests_require=[
		'pytest'
	],
	test_suite='Python-Module-Structure.test.test_package',
	cmdclass={
		'test': PyTest
	},
	include_package_data=True,
	classifiers=[
		#   3 - Alpha
		#   4 - Beta
		#   5 - Production/Stable
		'Development Status :: 3 - Alpha',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Build Tools',
		'License :: MIT License',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	],
	extras_require={
		'testing': [
			'pytest'
		]
	}
)
