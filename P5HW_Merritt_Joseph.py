#Joseph_Merritt
#18_Apr_24
#P5HW - Using Loops, Functions and Module Import

import random

def sum(num1, num2):
    print(f"{num1} + {num2}")
    result = num1 + num2
    return result
    
def guessing(answer):    
    guess = int(input("Enter an answer: "))
    results = 1
    while guess != answer:
        results += 1
        if guess < answer:
            print("Sorry, guess is to low")
        if guess > answer:
            print("Sorry, guess is to high")
        guess = int(input("Try again: "))
    print("Congratulations!!!! Your answer is correct ")       
    print(f"Number of guesses: {results}")

def main():
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)

    print("Welcome to Math Quiz")
    print()
    print("MAIN MENU")
    print("----------------------")
    print("1. Adding Random Numbers")
    print("2. Subracting Random Numbers")
    print("3. Exit")
    print()

    menu_opt = int(input("Please choose one of the menu options: "))


    while menu_opt != 3:
        if menu_opt == 1:
            answer = sum(num1, num2)
            guessing(answer)


        if menu_opt == 2:
            '''minus() ''' 
        menu_opt = int(input("Please choose one of the menu options: "))
main()
#At this point, loop has been broken
print("Program has ended, goodbye!") 