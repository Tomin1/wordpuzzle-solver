#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
#  Word Search Puzzle solving program
#  Copyright (C) 2012, Tomi Leppänen (aka Tomin)
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  

"""Word Search Puzzle solving program

Copyright (C) 2011-2012, Tomi Leppänen
This program comes with ABSOLUTELY NO WARRANTY. This is free software, 
and you are welcome to redistribute it under certain conditions.
See LICENSE file for more information.

Usage: 
    <the name of this file> -V # Prints version
    <the name of this file> -h # Prints this help
    <the name of this file> <filename> # Solves puzzle in <filename> named file.
"""

from util.printing import print_err, print_msg
from puzzle.tools import *

version = "v1"

def print_version(command):
    """Prints version infromation"""
    print_msg('''Words Search Puzzle solving program, version '''+version)

def print_usage(command):
    """Prints usage"""
    print_msg(__doc__.replace("<the name of this file>",command))

def main(command, *args):
    """Main function"""
    if len(args) != 1:
        print_err('''Invalid arguments!
See \''''+command+''' -h' for more information.''')
        return 1
    if args[0] == "-V":
        print_version(command)
        return 0
    if args[0] == "-h":
        print_usage(command)
        return 0
    puzzle = parse_from_file(args[0])
    puzzle.solve()
    print("\033[1mWords found:\033[0m")
    for word in puzzle.getSolved():
        print_msg(*word)
    print("\033[1mWords not found:\033[0m")
    for word in puzzle.getUnsolved():
        print_msg(*word)
    return 0

if __name__ == "__main__":
    import sys
    try:
        sys.exit(main(*sys.argv))
    except KeyboardInterrupt:
        raise
