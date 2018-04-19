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

import re

__author__ = "Alexander L. Hayes (@batflyer)"
__copyright__ = "Copyright (C) 2018 Alexander L. Hayes and Brian Ricks"
__credits__ = [
    "Alexander L. Hayes (@batflyer)",
    "Brian Ricks (@absolutefunk)",
    "Sriraam Natarajan (@boost-starai)",
    "Gautam Kunapuli (@gkunapuli)"
]

__license__ = "GPL-v3"
__version__ = "0.1.2"
__maintainer__ = "Alexander L. Hayes (@batflyer)"
__email__ = "alexander@batflyer.net"
__status__ = "Prototype"

mode_re = re.compile(r'[a-zA-Z0-9]*\(((\+|\-|\#)[a-zA-Z0-9]*,( )*)*(\+|\-|\#)[a-zA-Z0-9]*\)\.')

class modes:

    def __init__(self, background, target, loadAllLibraries=False,
                useStdLogicVariables=False, usePrologVariables=False,
                recursion=False, lineSearch=False, resampleNegs=False,
                treeDepth=None, maxTreeDepth=None, nodeSize=None,
                numOfClauses=None, numOfCycles=None, minLCTrees=None,
                incrLCTrees=None):

        self.target = target
        self.loadAllLibraries = loadAllLibraries
        self.useStdLogicVariables = useStdLogicVariables
        self.usePrologVariables = usePrologVariables
        self.recursion = recursion
        self.lineSearch = lineSearch
        self.resampleNegs = resampleNegs
        self.treeDepth = treeDepth
        self.maxTreeDepth = maxTreeDepth
        self.nodeSize = nodeSize
        self.numOfClauses = numOfClauses
        self.numOfCycles = numOfCycles
        self.minLCTrees = minLCTrees
        self.incrLCTrees = incrLCTrees

        relevant = [[attr, value] for attr, value in self.__dict__.items()
                    if (value is not False) and (value is not None)]

        background_knowledge = []
        for a, v in relevant:
            if (a in ['useStdLogicVariables', 'usePrologVariables'] and v == True):
                s = a + ': ' + str(v).lower() + '.'
                background_knowledge.append(s)
            elif a in ['target', 'bridgers', 'precomputes']:
                pass
            elif v == True:
                s = 'setParam: ' + a + '=' + str(v).lower() + '.'
                background_knowledge.append(s)
            else:
                s = 'setParam: ' + a + '=' + str(v) + '.'
                background_knowledge.append(s)

        for pred in background:
            self.inspect_mode_syntax(pred)
            background_knowledge.append('mode: ' + pred)

        # Write the newly created background_knowledge to a file: background.txt
        self.background_knowledge = background_knowledge
        self.write_to_file(background_knowledge, 'boosting/background.txt')

    def inspect_mode_syntax(self, example):
        """
        Uses a regular expression to check whether all of the examples in a list are in the correct form.
           Example:
              friends(+person, -person). ::: pass
              friends(-person, +person). ::: pass
              friends(person, person).   ::: FAIL
        """
        if not mode_re.search(example):
            raise(Exception('Error when checking background knowledge; incorrect syntax: ' + example + \
                            '\nBackground knowledge should only contain letters and numbers, of the form: ' + \
    'predicate(+var1, -var2).'))

    def write_to_file(self, content, path):
        '''Takes a list (content) and a path/file (path) and writes each line of the list to the file location.'''
        with open(path, 'w') as f:
            for line in content:
                f.write(line + '\n')
        f.close()

class BayesNet:
    # Basic class for storing nodes and edges in a Bayes Net, as well as the
    # trees learned along the way.

    def __init__(self):
        self.Nodes = []
        self.Edges = []
        self.Trees = []

def LearnDB2N(T, F):
    """
    Learns Bayes Network from an ordered set of targets and observed features.

    Description:
    Given a variable ordering of targets and observations, the goal is to learn
    a joint probability of targets and the variables which relate to them via
    Bayes Network. Consider the following dataset:

    +--------+--------+--------+-----+-------+----+
    | Person | Test_1 | Test_2 | EKG | ANGIO | VR |
    +--------+--------+--------+-----+-------+----+
    |   p1   |   0    |    1   |  1  |   1   |  1 |
    +--------+--------+--------+-----+-------+----+
    |   p2   |   1    |    1   |  1  |   1   |  0 |
    +--------+--------+--------+-----+-------+----+

    Test_1 and Test_2 are tests done on them at a certain point in time.
    EKG, ANGIO, and VR are procedures they received later in life.

    P(E, A, V, T) ~= P(E | T) P(A | E, T) P(V | E, A, T)

    Based on Algorithm 1 in "Discriminative Boosted Bayes Networks for Learn-
    ing Multiple Cardiovascular Procedures", but makes an assumption that
    T specifies both the elements and their ordering (i.e. instead of specif-
    ying both T and O variables, the ordering set in O is assumed to be the
    the same as it would be in T).

    @method LearnDB2N
    @param  {list}      T           ordered set of targets for the dataset,
                                    represented as a list of strings
    @param  {list}      F           set of observed features, also represen-
                                    ted as a list of strings
    @return {object}    BN

    Example:
    >>> targets = ['ekg', 'angio', 'vr']
    >>> observs = ['t1', 't2']
    >>> BayesNet = LearnDB2N(targets, observs)
    """

    # =================== Algorithm 1: LearnDB2N ======================
    # 1.        Input <T, F, O>
    # 2.        Output BN<N,E,T>
    # 3.        for i=1 to |T|; do
    # 4.            Ni = Ti
    # 5.            Ti = SFGBoost(Ti, <F, T<1:i-1>) P(Ti | F, T<1:i-1>)
    # 6.            Ei = GetFeatures(Ti)
    # 7.        endfor
    # 8.        return <N,E,T>

    BN = BayesNet()

    for i in range(len(T)):

        BN.Nodes += T[i]
        BN.Trees += SFGBoost()
        BN.Edges += GetFeatures(T[i])

        print(BN.Nodes, BN.Edges, BN.Trees)

    return BN

def GetFeatures(t):
    return [0]

def SFGBoost():
    """
    Performs softmax boosting.

    Based on Algorithm 2 in "Discriminative Boosted Bayes Networks for Learn-
    ing Multiple Cardiovascular Procedures".

    !!! This is not an actual implementation of SFGBoost, rather this is
        a series of wrappers which interact with a BoostSRL jar file.

        Visit BoostSRL on GitHub [1] or the documentation on the website [2]
        [1]: https://github.com/starling-lab/BoostSRL
        [2]: https://starling.utdallas.edu/software/boostsrl/wiki/cost-sensitive-srl/

    @method SFGBoost
    """



    return [0]

if __name__ == '__main__':

    m = modes([
        'Label(+id, #label).',
        'Dport(+id, #dport).',
        'Dur(+id, #dur).',
        'TotBytes(+id, #totbytes).',
        'TotPkts(+id, #totpkts).',
        'SrcBytes(+id, #srcbytes).',
        'Proto(+id, #proto).',
        'Dir(+id, #dir).',
        'Sport(+id, #sport).'
    ], 'Label', maxTreeDepth=2, nodeSize=1)

    targets = ['E', 'A', 'V']
    observations = ['t1', 't2']

    BayesNet = LearnDB2N(targets, observations)
