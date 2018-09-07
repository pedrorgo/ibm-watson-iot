#!/usr/bin/env python
# coding=utf-8

from setuptools import setup

package_name = 'ibm-watson-iot'
filename = package_name + '.py'

def get_version():
    import ast
    with open(filename) as input_file:
        for line in input_file:
            if line.startswith('__version__'):
                return ast.parse(line).body[0].value.s

def get_long_description():
    try:
        with open('README.md', 'r') as f:
            return f.read()
    except IOError:
        return ''

setup(
    name=package_name,
    version=get_version(),
    author='Pedro Oliveira',
    author_email='pedro.rui.oliveira@outlook.com',
    description='mqtt ping test',
    url='https://github.com/pedrorgo/ibm-watson-iot',
    long_description=get_long_description(),
    py_modules=[package_name],
    entry_points={
        'console_scripts': [
            'ibm-watson-iot=ibm-watson-iot:main'
            ]
        },
    license='License :: OSI Approved :: MIT License',
)
