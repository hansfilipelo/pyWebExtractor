#!/usr/bin/env python3

# Purpose: Generates "commander" file interface in HTML
# Creators: Jens Edhammer and Hans-Filip Elo

from os import listdir
from os.path import join,isfile
import textwrap

def listSourceDir(source):
    return [files for files in listdir(source) if not files.startswith(".")]

# -------------------------

def listTargetDir(target):
    return [dirOnly for dirOnly in listdir(target) if not isfile(join(target,dirOnly)) and not dirOnly.startswith(".")]

# -------------------------

def tableFromList(inList):
    output = "<table>" + '\n'

    htmlTableStart = textwrap.dedent("""\
        <tr>
            <td>
    """)
    htmlTableEnd = textwrap.dedent("""\
            </td>
        </tr>
    """)

    for data in inList:
        output += (htmlTableStart + data + htmlTableEnd)

    return output + "</table>"

# -------------------------

def returnHeader():
    return textwrap.dedent("""\
            <!DOCTYPE html>
            <html>

            <head>

            </head
            <!-- ------------ -->
            <body>
            """)

# -------------------------

def returnFooter():
    return (textwrap.dedent("""\
            </body>

            </html>
            """))

# -------------------------

def startTable():
    return textwrap.dedent("""\
            <table>
                <tr>
                    <td>
            """)

# -------------------------

def midTable():
    return (textwrap.dedent("""\
                    </td>
                    <td>
                    """))

# -------------------------

def endTable():
    return textwrap.dedent("""\
                        </td>
                    </tr>
                </table>
                """)

# -------------------------
