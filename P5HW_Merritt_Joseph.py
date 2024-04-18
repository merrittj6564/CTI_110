#Joseph_Merritt
#18_Apr_24
#P5HW - Using Loops, Functions and Module Import

import random

def sum(num1, num2):
    print(f"add {num1} ande {num2}")
    result = num1 + num2



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
        sum() 
    if menu_opt == 2:
        minus()
    menu_opt = int(input("Please choose one of the menu options: "))
#At this point, loop has been broken
print("Program has ended, goodbye!") 