#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
#  Some tools for working with puzzles
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
from puzzle.puzzle import Puzzle
import re

def parse_from_file(path):
    """Parses puzzle from file (in given path)"""
    puzzle = []
    words = []
    with open(path,'r') as fo:
        for row in fo:
            if row.startswith("#"):
                continue
            row = row[:-1]
            if not words:
                if len(row) > 0:
                    puzzle.append(row)
                    continue
                if len(row) == 0:
                    if puzzle:
                        words.append(True)
                    continue
            if words and len(row) > 0:
                words.append(row)
                continue
    puzzle = parse_from_table(puzzle)
    puzzle.add_words(words[1:])
    return puzzle

def parse_from_table(table):
    """Parses puzzle from table
    
    Mostly used by parse_from_file.
    """
    regex = re.compile(r'\t|\s+|,|;')
    for i in range(0,len(table)):
        table[i] = regex.split(table[i].strip().upper())
    return Puzzle(table)
