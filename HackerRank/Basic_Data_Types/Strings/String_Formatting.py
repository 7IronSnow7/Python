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

We will be using the variable number for these examples.
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
bina_number = bin(number)[2:] --> 
"""
#______________________
#      SOLUTION
#______________________

# Given

def main():
    print(bin(20)[2:])

main()