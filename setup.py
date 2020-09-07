# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in blackline/__init__.py
from blackline import __version__ as version

setup(
	name='blackline',
	version=version,
	description='App para gestión de flotillas de transporte personal.',
	author='Interconectando, Desarrollando y Automatizando, SAPI de CV',
	author_email='apps@interconectando.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
