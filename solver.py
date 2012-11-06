#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
#  This is supposed to solve Word search puzzles
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
from util.printing_tools import print_err
from puzzle.tools import *

version = "v1"

def print_version(command):
    print_msg('''Words Search Puzzle Solver, version '''+version+'''
Copyright (C) 2011-2012, Tomi Leppänen
This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
This is free software, and you are welcome to redistribute it
under certain conditions; type `show c' for details.''')

def main(args):
    if len(args) != 2:
        print_err("Invalid arguments!")
        return -1
    puzzle = parse_from_file(args[1])
    puzzle.solve()
    print("\033[1mWords found:\033[0m")
    for word in puzzle.getSolved():
        print(*word)
    print("\033[1mWords not found:\033[0m")
    for word in puzzle.getUnsolved():
        print(*word)

if __name__ == "__main__":
    import sys
    try:
        sys.exit(main(sys.argv))
    except KeyboardInterrupt:
        raise
