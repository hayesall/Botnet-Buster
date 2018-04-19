#!/usr/bin/env bash

#  Overview:
#      Name: boosting-setup.sh
#      Summary: A download/testing script for BoostSRL.
#      Author: Alexander L. Hayes (@batflyer)
#      Email: alexander.hayes@utdallas.edu
#      Copyright: Alexander L. Hayes and Brian Ricks
#      License: GPL-v3
#
#  Description:
#      The jar file can just as easily be downloaded
#      from GitHub. This downloads and tests the jar.
#
#  Usage:
#      $ bash boosting-setup.sh
#
#  Options:
#      -h     Display this help message and exit.
#      -s     Scripted mode. Do not prompt user to validate download.
#
#  License:
#  Copyright (c) 2018 Alexander L. Hayes and Brian Ricks
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  See <http://www.gnu.org/licenses/> or the license in the base of
#  this repository.

scriptmode=

while getopts "hs" o; do
  case ${o} in
    h)
      # Help and exit.
      head -n 36 $0 | tail -n +3 | sed 's/#//'
      exit 0
      ;;
    s)
      # Script mode, ignore interaction
      scriptmode=True
      ;;
    \?)
      # Error and exit
      echo "Error: -$OPTARG not recognized as a valid argument for boosting-setup.sh"
      exit 1
      ;;
    esac
done

function Downloader() {
  # Download the v1-0.jar from GitHub
  curl -k -L https://github.com/boost-starai/BoostSRL-Misc/blob/master/VersionHistory/Version1.0/v1-0.jar?raw=true > v1-0.jar
}

function Main() {
  if [[ ! $scriptmode ]]; then

    printf "Download BoostSRL v1-0.jar? (4.4 MB) [y/n] "
    read -r download

    if [[ "$download" = "y" ]]; then
      # User answered yes, proceed to downloading.
      Downloader
    else
      # User did not answer yes, assume no.
      echo "Did not download BoostSRL v1-0.jar"
    fi

  else
    # Script mode is true, download without user interaction.
    Downloader
  fi
}

Main
exit 0
