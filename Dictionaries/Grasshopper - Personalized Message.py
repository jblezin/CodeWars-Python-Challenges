##Problem Link: https://www.codewars.com/kata/5772da22b89313a4d50012f7

##Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

#Use conditionals to return the proper message:

#case                    return
#name equals owner      'Hello boss'
#otherwise              'Hello guest'


#Solution:
def greet(name, owner):
    
    match = {owner: 'Hello boss'}
    
    return match.get(name, 'Hello guest')                   #Option 1
    return "Hello boss" if name == owner else "Hello guest" #Option 2
    
greet('Daniel', 'Daniel')
