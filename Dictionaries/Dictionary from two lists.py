##Problem Link: https://www.codewars.com/kata/5533c2a50c4fea6832000101

##CThere are two lists, possibly of different lengths. The first one consists of keys, the second one consists of values. Write a function createDict(keys, values) that returns a dictionary created from keys and values. If there are not enough values, the rest of keys should have a None (JS null)value. If there not enough keys, just ignore the rest of values.

#Example 1:
#
#keys = ['a', 'b', 'c', 'd']
#values = [1, 2, 3]
#createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3, 'd': None}
#Example 2:
#
#keys = ['a', 'b', 'c']
#values = [1, 2, 3, 4]
#createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3}

#Solution:
import itertools

def create_dict(keys, values):

    return {keys: values for keys, values in itertools.zip_longest(keys, values) if keys is not None}

create_dict(['a', 'b', 'c'] , [1, 2, 3,8])
