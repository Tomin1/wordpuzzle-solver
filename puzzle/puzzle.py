#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
#  Puzzle presenting object
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

class Word:
    """Contains a word"""
    def __init__(self,word):
        self.word = word.upper()
        self.repr = word
        self.found = False
        self.position = None
        self.direction = None
    
    def __len__(self):
        return len(self.word)
    
    def __str__(self):
        return self.repr
    
    def __repr__(self):
        if self.found:
            return self.repr+str(self.position)+str(self.direction)
        else:
            return self.repr
    
    def setFound(self,position,direction):
        """Sets the word as found
        
        Sets the word as found and gives it position and direction.
        """
        self.found = True
        self.position = position
        self.direction = direction

class Puzzle:
    """Puzzle"""
    def __init__(self,puzzle):
        """Constructor
        
        This is the actual puzzle. 
        Requires parsed puzzle (see tools) as parameter.
        """
        self.puzzle = puzzle
        self.words = []
        self.charMap = CharacterMap(self)
    
    def __str__(self):
        string = ""
        for row in self.puzzle:
            string = "\n".join([string,str(row)])
        return string[1:]
    
    def add_words(self,words):
        """Adds words"""
        for word in words:
            self.words.append(Word(word))
    
    def solve(self):
        """Solves the puzzle"""
        for word in self.words:
            pair = word.word[0:2]
            for p in self.charMap.getVectors(pair):
                for pos,d in p:
                    if self.testWord(word,pos,d):
                        word.setFound(pos,d)
    
    def testWord(self,word,pos,d):
        """Tests for word 
        
        Tests for word in given position (tuple pos) to given 
        direction (int d).
        """
        x,y = pos
        i = 0
        for c in self.getVector(pos,d,len(word)):
            if word.word[i] != c:
                return False
            i = i + 1
        return True
    
    def getCharacters(self):
        """Generator, yields all characters"""
        x = -1
        y = 0
        while y < len(self.puzzle):
            x = x + 1
            if x < len(self.puzzle[y]):
                yield (self.puzzle[y][x],(x,y))
            else:
                y = y + 1
                x = 0
        return
    
    def getVector(self,begin_pos,direction,length):
        """Generator, yields characters
        
        Yields characters from given position to given direction
        """
        if direction == 4:
            return
        x,y = begin_pos
        for i in range(0,length):
            try:
                yield self.puzzle[y][x]
            except IndexError:
                return
            x = x + direction % 3 - 1
            y = y + direction // 3 - 1
        return
    
    def getSolved(self):
        """Generator, yields found words"""
        for word in self.words:
            if word.found:
                yield (word, word.position)
        return
    
    def getUnsolved(self):
        """Generator, yields words that aren't found"""
        for word in self.words:
            if not word.found:
                yield (word, word.position)
        return

class CharacterMap:
    """Character map"""
    def __init__(self,puzzle):
        """Constructor, requres Puzzle-object as parameter"""
        self.map = {}
        for c,pos in puzzle.getCharacters():
            for d in range(0,9):
                if d == 4:
                    continue
                pair = [i for i in puzzle.getVector(pos,d,2)]
                if len(pair) < 2:
                    continue
                try:
                    self.map["".join(pair)].append((pos,d))
                except KeyError:
                    self.map["".join(pair)] = [(pos,d)]
    
    def __str__(self):
        return str(self.map)
    
    def getVectors(self,needle):
        """Generator, yields all vectors in the map"""
        for i in self.map:
            if i == needle:
                yield self.map[i]
        return
