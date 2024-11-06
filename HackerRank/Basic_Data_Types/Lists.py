#______________________
#      INFORMATION
#______________________

"""_summary_
    Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.
"""
#______________________
#      SOLUTION
#______________________

# Given
if __name__ == '__main__':
    N = int(input())
    L = []
    # code goes here
    
    for i in range(0, N):
        cmd = input().split()
        
        if cmd[0] == "insert":
            L.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "append":
            L.append(int(cmd[1]))
        elif cmd[0] == "print":
            print(L)
        elif cmd[0] == "remove":
            L.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            L.sort()
        elif cmd[0] == "pop":
            L.pop()
        elif cmd[0] == "reverse":
            L.reverse()
    
