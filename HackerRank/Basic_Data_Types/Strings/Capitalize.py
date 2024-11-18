#______________________
#      INFORMATION
#______________________

"""_summary_
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
"""
#______________________
#      SOLUTION
#______________________

# Given
# Now there is two ways to do it:
# The first is splitting up the string and capitalizing each word
# and adding it back to the variable known as 'passport_name'
def solve(s):
    # Your code goes here
    name = s.split(" ")
    
    # Storing the capitalized name here
    passport_name = ""
    
    for c in name:
        passport_name += f"{c.capitalize()} "
    return passport_name 
#____________________________________________________________  

def solve2(s):
    # This is the second way which is basically a condensed version of one
    return ' '.join(word.capitalize() for word in s.split(' '))
#_____________________________________________________________

if __name__ == '__main__':
    # This importation wasn't necessary in vs code
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input("Please enter a name: ") #<---- Instruction purpose use only

    result = solve(s)
    result2 = solve2(s)

    print(result + '\n')
    print(result2 + '\n')
    
