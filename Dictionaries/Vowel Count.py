##Problem Link: https://www.codewars.com/kata/54ff3102c1bad923760001f3

##Return the number (count) of vowels in the given string.

#We will consider a, e, i, o, u as vowels for this Kata (but not y).

#The input string will only consist of lower case letters and/or spaces.

#Solution:
def get_count(sentence):
    return sum(map(sentence.lower().count, "aeiou")) #Option 1
    return len([vowel for vowel in sentence if vowel in 'aeoiu']) #Option 2
    
get_count('sentence')
