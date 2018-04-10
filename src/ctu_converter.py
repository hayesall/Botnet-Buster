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

from os import path

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

def binetflow_converter(path_to_file, dropCols=[], verbosity=False):
    """
    Takes a path to a .binetflow, reads the file, and returns a dataframe.

    @method binetflow_converter
    @param  {str}       path_to_file        path to the .binetflow file
    @param  {list}      dropCols            list of strings representing columns to be dropped.
    @param  {bool}      verbosity           verbose mode (True = more printing)
    @return {df}        binetflow_df        contents of the .binetflow file as a dataframe

    Example:
    >>> flow = binetflow_converter('CTU-13-Dataset/1/capture20110810.binetflow', dropCols=['StartTime'])
    """

    # Read the .binetflow csv located at path_to_file, drop columns which are less useful.
    binetflow_df = pd.read_csv(path_to_file)

    if dropCols:
        binetflow_df = binetflow_df.drop(dropCols, axis=1)

    # Debug option, show the columns:
    if verbosity > 0:
        print(binetflow_df)

    return binetflow_df

def dataframe_to_relations(path_to_file, df, verbosity=False):
    """
    Converts a dataframe into a set of positives, negatives, and facts
    in the manner used by BoostSRL (https://github.com/starling-lab/BoostSRL).
    The output is written to 'path_to_file'.

    @method dataframe_to_relations
    @param  {str}       path_to_file        output file to be written to
    @param  {object}    df                  pandas dataframe
    @param  {bool}      verbosity           verbose mode (True = more printing)
    @return {}

    Example:
    >>> flow = binetflow_converter('CTU-13-Dataset/1/capture20110810.binetflow')
    >>> dataframe_to_relations(flow)
    """

    headers = list(df)
    label = headers[-1]
    print(label)
    print(headers)

    for _, row in df.iterrows():
        for header in headers:
            print(row[header])
        exit()

def main():

    # Instantiate an argument parser to help describe the program.
    parser = argparse.ArgumentParser(
        description='''Converts .binetflow files into the relational format
                    used by BoostSRL.''',
        epilog='''Copyright (C) 2018 Alexander L. Hayes and Brian Ricks.
                    Distributed under the terms of the GPL-v3. A full
                    copy of the license is available in the base of the
                    repository, or online at <http://www.gnu.org/licenses/>'''
    )

    parser.add_argument('-v', '--verbose', action="store_true",
        help='Increase verbosity to help with debugging')
    parser.add_argument('-f', '--file', type=str,
        help='Specify path to .binetflow')
    parser.add_argument('-o', '--output', type=str,
        default='binetflow.out',
        help='''Specify path to the output file where predicates will be
                written. If an output file is not specified, defaults to
                binetflow.out in the same directory.''')

    args = parser.parse_args()

    # If verbose was set to true, increment the verbosity.
    if args.verbose:
        v = True
    else:
        v = False

    flow = binetflow_converter(args.file, dropCols=['StartTime'], verbosity=v)
    dataframe_to_relations(args.output, flow, verbosity=v)

if __name__ == '__main__':
    main()
