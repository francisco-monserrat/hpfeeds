#!/usr/bin/env python

from distutils.core import setup

setup(
	name='hpfeeds',
	version='1.0',
	description='hpfeeds module',
	author='Mark Schloesser',
	author_email='ms@mwcollect.org',
	url='https://github.com/rep/hpfeeds',
	license='GPL',
	package_dir = {'': 'lib'},
	py_modules = ['hpfeeds'],
	scripts=['cli/hpfeeds-client']
)
