# def enchant_and_attack(target_health, damage, weapon):
#     enchanted_damage = damage + 10
#     new_health = target_health - enchanted_damage
#     enchanted_weapon = f"enchanted {weapon}"

#     return enchanted_weapon, new_health


# # Don't modify below this line


# def test(target_health, damage, weapon):
#     print("The target has", target_health, "health.")
#     print(weapon, "base damage:", damage, "Enchanting and attacking")
#     enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
#     print("The target has been attacked with the", enchanted_weapon)
#     print("The target has", new_health, "health remaining.")
#     print("=====================================")


# def main():
#     test(100, 50, "sword")
#     test(500, 100, "axe")
#     test(1000, 250, "bow")


# main()


# def findClosestNumber(nums: list[int]) -> int:

    
# nums = [-4, -2, 1, 4, 8]
# nums2 = [4, 4, 4, 2, -2]
# def main():
#     findClosestNumber(nums)
#     findClosestNumber(nums2)
    
    


# def weirdNotWeird(n):

#     if(n % 2 == 0 and 2 <= n <= 5):
#         print("Not Weird")
#     elif(6 <= n <= 20):
#         print("Weird")
#     else:
#         print("Not Weird")
    

# def main():
#     weirdNotWeird(5)
    
# main()

# print(7.1e-2)
sentence = "wall street journal"
sentence1 = "this is pig latin"
def pigLatinSentence(sentence):
    
    vowels = ["a", "e", "i", "o", "u" ]
    
    words = sentence.split(" ")
    latin_words = []
    
    for word in words:
        if(word[0] in vowels):
            latin_word = word + "way"
            
        else:
            for index, character in enumerate(word):
                if(character in vowels):
                    latin_word = word[index:] + word[:index] + "ay"
                    break
        latin_words.append(latin_word)
    
    print(latin_words)            
def main():
    pigLatinSentence(sentence)
    print("\n---------------------------------")
    pigLatinSentence(sentence1)

main()