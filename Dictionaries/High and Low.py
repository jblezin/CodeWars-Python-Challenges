##Problem Link: https://www.codewars.com/kata/554b4ac871d6813a030000354

##In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

#Examples
#
#high_and_low("1 2 3 4 5")  # return "5 1"
#
#high_and_low("1 2 -3 4 5") # return "5 -3"
#
#high_and_low("1 9 3 4 -5") # return "9 -5"
#
#Notes
#
#All numbers are valid Int32, no need to validate them.
#There will always be at least one number in the input string.
#Output string must be two numbers separated by a single space, and highest number is first.

#Solution:
def high_and_low(numbers):
    numbers = [int(value) for value in numbers.split()]
    
    return f'{max(numbers)} {min(numbers)}'
    
high_and_low("437 560 543 -783 -271 28 -641 406 112 512 -777 -945 -500 -717 -398")
