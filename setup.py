#!/usr/bin/env python
import os
from setuptools import setup, find_packages

long_description = open(
    os.path.join(
        os.path.dirname(__file__),
        'README.md'
    )
).read()

setup(
    name='LR35902',
    version='0.1',
    author='John Shanahan',
    author_email='shanahan.jrs@gmail.com',
    url='https://github.com/shanahanjrs/LR35902',
    description='GameBoy LR35902 emulator',
    long_description=long_description,
    packages=find_packages('.'),
    install_requires=[],
    tests_require=[],
)

