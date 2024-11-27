# String Validators

#______________________
#      INFORMATION
#______________________

"""_summary_
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words
Returns

string: the resulting string
Input Format
The one line contains a string consisting of space separated words.

Sample Input

this is a string   
Sample Output

this-is-a-string

Note:
Splitting a string: text = "this is a text"
    split_text = text.split(" ") <--- Whatever is inside the parenthesis
    Output = ['this', 'is', 'a', 'text']
    
Joining a string: joined_text = "-".join(split_text)
    Output = this-a-text
"""
#______________________
#      SOLUTION
#______________________


# Given
def split_and_join(line):
    # Your code goes here
    new_line = line.split(" ")
    joined_line = "-".join(new_line)
    return joined_line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
