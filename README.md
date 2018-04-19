# Botnet-Buster

**[Alexander L. Hayes](https://github.com/batflyer)** and **[Brian Ricks](https://github.com/absolutefunk)**

Final project for Professor Sriraam Natarajan's spring seminar on Statistical Relational Learning. Applying SRL to the problem of discerning botnet traffic from normal traffic.

## Setup

**Clone the repository and download the CTU-13-Dataset**  
* `git clone https://github.com/batflyer/Botnet-Buster.git`
* `cd Botnet-Buster`
* `bash downloader.sh`

**Download BoostSRL**  
* `cd boosting`
* `bash boosting-setup.sh`

**Convert a .binetflow to BoostSRL format**  
* `python botnetbuster/ctu_converter.py -o train -f CTU-13-Dataset/1/capture20110810.binetflow`

**Learn Discriminative Boosted Bayesian Network**  
* `python botnetbuster/disc_boost.py`

## Converting .binetflow to BoostSRL format:

`ctu_converter.py` is a Python script for converting a .binetflow file to the relational format used by BoostSRL. Its design is intended for commandline interaction (options may be viewed with the `-h` flag).

Convert a .binetflow to a set of facts and positive examples, creating `posEx.txt` and `facts.txt`.

* `python botnetbuster/ctu_converter.py -o train -f CTU-13-Dataset/1/capture20110810.binetflow`

## Weka Discretizations and Baselines

* `curl -L http://prdownloads.sourceforge.net/weka/weka-3-9-2.zip -o weka-3-9-2.zip`
* `unzip weka-3-9-2.zip`

## Variable Ordering

.binetflow has the following labels:

`StartTime`, `Dur`, `Proto`, `SrcAddr`, `Sport`, `Dir`, `DstAddr`, `Dport`, `sTos`, `dTos`, `TotPkts`, `TotBytes`, `SrcBytes`, `Label`

Of these labels, the target is the value in the `Label` column, and the variable ordering is: `Dport`, `Dur`, `TotBytes`, `TotPkts`, `SrcBytes`, `Proto`, `Dir`, `Sport`

## BoostSRL

Botnet-Buster uses [BoostSRL](https://github.com/starling-lab/BoostSRL) as the learning and inference engine for Discriminative Boosted Bayesian Networks. Most of these operations are automated, but a copy of the BoostSRL jar file should be downloaded with the `boosting-setup.sh` script in the `boosting` directory.

* `cd boosting/`
* `bash boosting-setup.sh`

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

A full [copy of the license](https://github.com/batflyer/Botnet-Buster/blob/master/LICENSE) is available in the base of this repository. For more information, see https://www.gnu.org/licenses/

## Attribution

* `progress.py` was created by Vladimir Ignatev (@vladignatyev) and distributed under the terms of the MIT License. Discussion can be viewed on the [GitHub Gist page](https://gist.github.com/vladignatyev/06860ec2040cb497f0f3).
* `disc_boost.py` uses code from [starling-lab/boostsrl-python-package](https://github.com/starling-lab/boostsrl-python-package) under the terms of the GPL-v3 License, the portions to validate and set modes files was used here.

## References

* [1] Garcia, Sebastian. Malware Capture Facility Project. Retrieved from https://stratosphereips.org
