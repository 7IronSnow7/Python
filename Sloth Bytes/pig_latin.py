sentence = "wall street journal"
sentence1 = "this is pig latin"
def pigLatinSentence(sentence):
    
    # For words that begin with a vowel (a, e, i, o, u) add way
    vowel = ["a", "e", "i", "o", "u"]
    
    words = sentence.split(" ")
    latin_words = []
    
    for word in words:        
        if(word[0] in vowel):
            latin_word = word + "way"
            
        # Look for the first present vowel letter in the word
        else:
            for index, char in enumerate(word):
                if(char in vowel):
                    latin_word = word[index:] + word[:index] + "ay"
                    break
        latin_words.append(latin_word)
    
    
    print(latin_words)
                        

def main():
    pigLatinSentence(sentence)
    
main()