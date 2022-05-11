from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name='phaser',
    version='0.0.1',
    description='Phaser phase estimation library.',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/atspaeth/phaser',
    author='BIRDS Lab',
    classifiers=[
        'Development Status :: 2 - Beta',
        'Programming Language :: Python :: 3'],
    packages=find_packages(exclude=()),
    install_requires=['numpy', 'scipy'])
