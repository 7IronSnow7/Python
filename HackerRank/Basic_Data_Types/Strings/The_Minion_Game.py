# The Minion Game
#______________________
#      INFORMATION
#______________________

"""_summary_
Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""
#______________________
#      SOLUTION
#______________________

# Given
def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    stuart_score, kevin_score = 0, 0
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
            
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")
    
        
if __name__ == '__main__':
    s = input("Please input some text: ")
    minion_game(s)