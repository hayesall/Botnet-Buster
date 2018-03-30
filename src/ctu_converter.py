"""
Copyright (C) 2018 Alexander L. Hayes and Brian Ricks

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program (at the base of this repository). If not,
see <http://www.gnu.org/licenses/>
"""

from __future__ import print_function

import numpy as np
import pandas as pd

import argparse


__author__ = "Alexander L. Hayes (@batflyer)"
__copyright__ = "Copyright (C) 2018 Alexander L. Hayes and Brian Ricks"
__credits__ = [
    "Alexander L. Hayes (@batflyer)",
    "Brian Ricks (@absolutefunk)",
    "Sriraam Natarajan (@boost-starai)",
    "Gautam Kunapuli (@gkunapuli)"
]

__license__ = "GPL-v3"
__version__ = "0.0.1"
__maintainer__ = "Alexander L. Hayes (@batflyer)"
__email__ = "alexander@batflyer.net"
__status__ = "Prototype"

class Arguments:

    def __init__(self):

        parser = argparse.ArgumentParser(
            description="Converts .binetflow files into the relational format used by BoostSRL.",
            epilog="Copyright 2018 Alexander L. Hayes and Brian Ricks. GPL-v3."
        )

        parser.add_argument(
            '-v', '--verbose', action="store_true",
            help='Increase verbosity to help with debugging')
        parser.add_argument(
            '-f', '--file', type=str,
            help='Specify path to .binetflow')

        self.args = parser.parse_args()

def main():

    args = Arguments().args
    print(args)
    

if __name__ == '__main__':
    main()
