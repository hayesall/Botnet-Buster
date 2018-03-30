'''
Setup file for the Python portions of Botnet-Buster.

Heavily based on the setup file Alexander L. Hayes (@batflyer) wrote for
boostsrl-python-package. Licensed under the GPL-v3.
>>> https://github.com/starling-lab/boostsrl-python-package/blob/master/setup.py
'''

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # Attributes
    name='botnet_buster',
    packages=['botnet_buster'],
    author='Alexander L. Hayes (batflyer)',
    author_email='alexander@batflyer.net',
    version='0.0.1',
    description="Final project for Professor Sriraam Natarajan's 2018 Spring Seminar on SRL.",
    long_description=long_description,
    url='https://github.com/batflyer/Botnet-Buster',
    download_url='https://github.com/batflyer/Botnet-Buster/archive/0.0.1.tar.gz',

    # License
    license='GPL-3.0',

    classifiers=[
        # Current development status
        'Development Status :: 3 - Alpha',

        # Intended Audiences
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',

        # License
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # OS
        'Operating System :: POSIX :: Linux',

        # Supported Python Versions
        # Check build status: https://travis-ci.org/batflyer/boostsrl-python-package
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        
        # Topic
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],

    keywords='statistical-learning pattern-classification',

    install_requires = ['pandas'],
    extras_require={
        'test': ['coverage']
    }
)
