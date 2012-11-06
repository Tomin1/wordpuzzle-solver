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
        self.found = True
        self.position = position
        self.direction = direction

class Puzzle:
    def __init__(self,puzzle):
        self.puzzle = puzzle
        self.words = []
        self.charNumbers = self.countCharacters()
        self.charMap = CharacterMap(self)
    
    def __str__(self):
        string = ""
        for row in self.puzzle:
            string = "\n".join([string,str(row)])
        return string[1:]
    
    def iterateCharacters(self):
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
    
    def add_words(self,words):
        for word in words:
            self.words.append(Word(word))
    
    def countCharacters(self):
        characters = {}
        for row in self.puzzle:
            for char in row:
                try:
                    characters[char] = characters[char] + 1
                except KeyError:
                    characters[char] = 1
        return characters
    
    def solve(self):
        for word in self.words:
            pair = word.word[0:2]
            for p in self.charMap.iterateVectors(pair):
                for pos,d in p:
                    if self.testWord(word,pos,d):
                        word.setFound(pos,d)
    
    def testWord(self,word,pos,d):
        x,y = pos
        i = 0
        for c in self.iterateVector(pos,d,len(word)):
            if word.word[i] != c:
                return False
            i = i + 1
        return True
    
    def iterateVector(self,begin_pos,direction,length):
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

class CharacterMap:
    def __init__(self,puzzle):
        self.map = {}
        for c,pos in puzzle.iterateCharacters():
            for d in range(0,9):
                if d == 4:
                    continue
                pair = [i for i in puzzle.iterateVector(pos,d,2)]
                if len(pair) < 2:
                    continue
                try:
                    self.map["".join(pair)].append((pos,d))
                except KeyError:
                    self.map["".join(pair)] = [(pos,d)]
    
    def __str__(self):
        return str(self.map)
    
    def iterateVectors(self,needle):
        for i in self.map:
            if i == needle:
                yield self.map[i]
        return
