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
    >>> observs = ['t1', t2]
    >>> BayesNet = LearnDB2N(targets, observs)
    """
    pass

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
    pass

if __name__ == '__main__':
    pass
