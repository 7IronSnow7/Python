#______________________
#      INFORMATION
#______________________

"""_summary_
Handling Exceptions
The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause to specify handlers for different exceptions.

#Code
try:
    print 1/0
except ZeroDivisionError as e:
    print "Error Code:",e
Output

Error Code: integer division or modulo by zero

Task

You are given two values  and .
Perform integer division and print .

Input Format

The first line contains , the number of test cases.
The next  lines each contain the space separated values of  and .

Constraints

Output Format

Print the value of .
In the case of ZeroDivisionError or ValueError, print the error code.

Sample Input

3
1 0
2 $
3 1
Sample Output

Error Code: integer division or modulo by zero
Error Code: invalid literal for int() with base 10: '$'
3
"""
#______________________
#      SOLUTION
#______________________
# link: https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
# for _ in range(int(input())):
#     try:
#         a, b = input().split()
#         print(int(a) // int(b))
#     except ZeroDivisionError as z:
#         print(f"Error Code: {z}")
#     except ValueError as v:
#         print(f"Error Code: {v}")

# Gonna use this file to run some tests for a different issue:
