##Problem Link: https://www.codewars.com/kata/5631ac5139795b281d00007d

##Design a data structure that supports the following two operations:

#addWord (or add_word) which adds a word,
#search which searches a literal word or a regular expression string containing lowercase letters #"a-z" or "." where "." can represent any letter
#You may assume that all given words contain only lowercase letters.
#
#Examples
#
#addWord("bad")
#addWord("dad")
#addWord("mad")
#
#search("pad") === false
#search("bad") === true
#search(".ad") === true
#search("b..") === true

#Solution:
from re import fullmatch

class WordDictionary:
    def __init__(self):
        self.add_wordMap = {}
        self.searchMap = {}

    def add_word(self, word):
        self.add_wordMap[word] = word

    def search(self, word):
        return any(fullmatch(word,value) for value in self.add_wordMap.values())
