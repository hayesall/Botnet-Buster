#!/bin/bash

#  Overview:
#      Name: download.sh
#      Summary: A download script for the CTU-13-Dataset.
#      Author: Alexander L. Hayes (@batflyer)
#      Email: alexander.hayes@utdallas.edu
#      Copyright: Copyright (c) 2018, Alexander L. Hayes
#      License: NULL (not provided currently)
#  
#  Description:
#      It's generally bad practice to push large data
#      sets to GitHub. Download the data separately.
#  
#  Usage:
#      $ bash download.sh
#  
#  License:
#      Licensing information is not currently provided.
#      Usage rights are not granted by the author.

scriptmode=

while getopts "hs" o; do
    case ${o} in
	h)
	    # Help
	    head -n 20 $0 | tail -n +3 | sed 's/#  //'
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
