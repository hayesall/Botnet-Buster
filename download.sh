#!/bin/bash

#  Overview:
#      Name: download.sh
#      Summary: A download script for the CTU-13-Dataset.
#      Author: Alexander L. Hayes (@batflyer)
#      Email: alexander.hayes@utdallas.edu
#      Copyright: Alexander L. Hayes and Brian Ricks
#      License: GPL-v3
#  
#  Description:
#      It's generally bad practice to push large data
#      sets to GitHub. Download the data separately.
#  
#  Usage:
#      $ bash download.sh
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
	    # Help
	    head -n 32 $0 | tail -n +3 | sed 's/#  //'
	    exit 0
	    ;;
	s)
	    # Script mode, ignore interaction.
	    scriptmode=True
	    ;;
	\?)
	    echo "Error: -$OPTARG not recognized as a valid argument for download.sh"
	    exit 1
	    ;;
    esac
done

function Downloader() {
    # Download the .tar.bz of the CTU-13-Dataset using curl.
    curl -k -L https://mcfp.felk.cvut.cz/publicDatasets/CTU-13-Dataset/CTU-13-Dataset.tar.bz2 > CTU-13-Dataset.tar.bz2
    
    # Use unar to extract from the archive.
    unar CTU-13-Dataset.tar.bz2
    
    # Perform cleanup
    rm -f CTU-13-Dataset.tar.bz2
}

function Cleanup() {
    # Perform cleanup by removing the archive.
    rm -f CTU-13-Dataset.tar.bz2
}

function Main() {
    if [[ ! $scriptmode ]]; then
	
	printf "Download CTU-13-Dataset? (1.9 GB) [y/n] "
	read -r download
	
	if [[ "$download" = "y" ]]; then
	    Downloader

	    printf "Remove the .tar.bz2 archive? [y/n]"
	    read -r removal

	    if [[ "$removal" = "y" ]]; then
		Cleanup
	    else
		echo "Did not remove CTU-13-Dataset.tar.bz2"
	    fi
	    
	else
	    echo "Exited without downloading."
	    exit 0
	fi
    else
	Downloader
    fi
}

Main
