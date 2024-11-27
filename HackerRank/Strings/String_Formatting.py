#______________________
#      INFORMATION
#______________________

"""_summary_
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
Function Description

Complete the print_formatted function in the editor below.

print_formatted has the following parameters:

int number: the maximum value to print
Prints

The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of  and the values should be separated by a single space.

Input Format

A single integer denoting .

For the solutions sake here is a cheat sheet so you won't have to look up the formats like I did:
P.S Python has built in methods to convert to the specified formats above.

We will be using the variable "number" for these examples.
number = 20
TO GET A DECIMAL OF AN INTEGER:
deci_number = str(number)

TO GET AN OCTAL OF AN INTEGER:
octa_number = oct(number) --> 0o24 
But we don't want the first two digits so we are going to slice them
octa_number = oct(number)[2:] --> 24
P.S we will do that for the rest of the string formatters needed for this solution

TO GET A HEXADECIMAL OF AN INTEGER:
hex_number = hex(number)[2:] --> 14

TO GET A BINARY OF AN INTEGER:
bina_number = bin(number)[2:] --> 10100
"""
#______________________
#      SOLUTION
#______________________

# Given
def print_formatted(number):
    # your code goes here
    # create the specified width for the solution
    width = len(bin(number)[2:])
    
    for num in range(1, number + 1):
        deci = str(num)
        octa = oct(num)[2:]
        hexa = hex(num)[2:].upper()
        bina = bin(num)[2:]
        print(deci.rjust(width), octa.rjust(width), hexa.rjust(width), bina.rjust(width))
    
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)