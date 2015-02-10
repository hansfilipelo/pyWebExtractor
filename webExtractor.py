#!/usr/bin/env python3

# Purpose: Generates "commander" file interface in HTML
# Creators: Jens Edhammer and Hans-Filip Elo

import argparse
from printOuts import *

# Parse arguments
# ---------------------------------
description = """\
    Script for generating HTML page.
"""

parser = argparse.ArgumentParser(description=description)
parser.add_argument("-s","--source", metavar="SOURCEDIR", dest="source")
parser.add_argument("-t","--target", metavar="TARGETDIR", dest="target")

opts = parser.parse_args()
# ---------------------------------

print(returnHeader())

print(startTable())

print(tableFromList(listSourceDir(opts.source)))

print(midTable())

print(tableFromList(listTargetDir(opts.target)))

print(endTable())

print(returnFooter())
