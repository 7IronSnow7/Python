#______________________
#      INFORMATION
#______________________

"""_summary_
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Sample Input

ABCDCDC
CDC
Sample Output

2
"""
#______________________
#      SOLUTION
#______________________

# Given

def count_substring(string, sub_string):
    # Code goes here
    
    # Create variables to keep track of occurences
    # and where to start searching
    
    start = 0
    count = 0
    
    while start < len(string):
        pos = string.find(sub_string, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)