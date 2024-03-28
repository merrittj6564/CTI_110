#Joseph_Merritt
#28_Mar_24
#P4HW1 - Using the range function

score_list = []

Score = int(input("How many scores do you want to enter? "))

for number in range(Score):
    num1 = int(input(f"Enter score #{number+1}: "))
    while num1 < 0 or num1 > 100:
        print("INVALD Score enterned!!!! ")
        print("Score should be between 0 and 100")
        num1 = int(input(f"Enter score #{number+1} again: "))
    score_list.append(num1)
print("\n------------Results-------------")

list_min = min(score_list)
print(f"Lowest Score: {list_min}")

score_list.remove(list_min)
print(f"Modified List: {score_list}")

list_avr = sum(score_list) / Score
print(f"Scores Average: {list_avr}")

if list_avr >= 90:
    print("Grade: A")

elif list_avr >= 80:
 print("Grade: B")

elif list_avr >= 70:
 print("Grade: C")

elif list_avr <= 69: 
    print("Grade: F")

print("------------------------------------")