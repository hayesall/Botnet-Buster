# Botnet-Buster

**[Alexander L. Hayes](https://github.com/batflyer)** and **[Brian Ricks](https://github.com/absolutefunk)**

Final project for Professor Sriraam Natarajan's spring seminar on Statistical Relational Learning. Applying SRL to the problem of discerning botnet traffic from normal traffic.

## Setup

* `git clone https://github.com/batflyer/Botnet-Buster.git`
* `cd Botnet-Buster`
* `bash downloader.sh`

## Converting .binetflow to BoostSRL format:

`ctu_converter.py` is a Python script for converting a .binetflow file to the relational format used by BoostSRL. Its design is intended for commandline interaction (options may be viewed with the `-h` flag).

Convert a .binetflow to a set of facts and positive examples, creating `posEx.txt` and `facts.txt`.

* `python src/ctu_converter.py -f CTU-13-Dataset/1/capture20110810.binetflow`

## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

A full [copy of the license](https://github.com/batflyer/Botnet-Buster/blob/master/LICENSE) is available in the base of this repository. For more information, see https://www.gnu.org/licenses/

## Attribution

* `progress.py` was created by Vladimir Ignatev (@vladignatyev) and distributed under the terms of the MIT License. Discussion can be viewed on the [GitHub Gist page](https://gist.github.com/vladignatyev/06860ec2040cb497f0f3).

## References

* [1] Garcia, Sebastian. Malware Capture Facility Project. Retrieved from https://stratosphereips.org
