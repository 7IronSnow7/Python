#______________________
#      INFORMATION
#______________________

"""_summary_
You are given a two lists  and . Your task is to compute their cartesian product X.

Example

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.

Input Format

The first line contains the space separated elements of list .
The second line contains the space separated elements of list .

Both lists have no duplicate integer elements.

Constraints



Output Format

Output the space separated tuples of the cartesian product.

Sample Input

 1 2
 3 4
Sample Output

 (1, 3) (1, 4) (2, 3) (2, 4)
"""
#______________________
#      SOLUTION
#______________________
# link: https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

from itertools import product

def solution(A, B):
    
    result = list(product(A, B))
    result_str = " ".join(str(pair) for pair in result) 
    return result_str
    
def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    print(solution(A, B))
    
main()