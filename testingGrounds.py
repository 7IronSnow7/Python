n = 8
numbers = 154, 161, 167, 170, 171, 174, 176, 182

def adding_all_numbers(n, numbers):
    sum = 0
    
    for number in numbers:
        sum += number
        
    print(sum)
    
def main():
    adding_all_numbers(n, numbers)
    

main()
    