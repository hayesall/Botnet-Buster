#!/bin/bash

# Overview:
#      Name: download.sh
#      Summary: A download script for the CTU-13-Dataset.
#      Author: Alexander L. Hayes (@batflyer)
#      Email: alexander.hayes@utdallas.edu
#      Copyright: Copyright (c) 2018, Alexander L. Hayes
#      License: NULL (not provided currently)
# 
# Description:
#      It's generally bad practice to push large data
#      sets to GitHub. Download the data separately.
# 
# Usage:
#      $ bash download.sh
# 
# License:
#      Licensing information is not currently provided.
#      Usage rights are not granted by the author.

# Download the .tar.bz of the CTU-13-Dataset using curl.
curl -L https://mcfp.felk.cvut.cz/publicDatasets/CTU-13-Dataset/CTU-13-Dataset.tar.bz2 > CTU-13-Dataset.tar.bz2

# Use unar to extract from the archive.
unar CTU-13-Dataset.tar.bz2
