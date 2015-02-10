#!/usr/bin/env python3

# Purpose: Generates "commander" file interface in HTML
# Creators: Jens Edhammer and Hans-Filip Elo

import sys
import os

def createFolderInterface(source, target):
    for files in os.listdir(source):
        if not files.startswith("."):
            print(files)

    print('\n' + "Break" + '\n')

    for dirOnly in os.listdir(target):
        if not os.path.isfile(os.path.join(target,dirOnly)):
            if not dirOnly.startswith("."):
                print(dirOnly)


createFolderInterface(".","/home/fille/")
