##Problem Link: https://www.codewars.com/kata/57a93f93bb9944516d0000c1/python

##In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:

#>>> d = Dictionary()
#
#>>> d.newentry('Apple', 'A fruit that grows on trees')
#
#>>> print(d.look('Apple'))
#A fruit that grows on trees
#
#>>> print(d.look('Banana'))
#Can't find entry for Banana
#Good luck and happy coding!

#Solution:
class Dictionary():
    def __init__(self):
        self.newentryMap = {}
        
    def newentry(self, word, definition):
        self.newentryMap[word] = str(definition)

    def look(self, key):
        return self.newentryMap.get(key, f"Can't find entry for {key}")
        
        
