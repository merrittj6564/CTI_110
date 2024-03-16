#Joseph Merritt
#16 March 2024
#P3HW1
#Grading Lists

# This program takes a number grade , determines average and displays letter grade for average.
nums = []

# Enter grades for six modules

nums.append(float(input("Enter a grade for Module 1: ")))
nums.append(float(input("Enter a grade for Module 2: ")))
nums.append(float(input("Enter a grade for Module 3: ")))
nums.append(float(input("Enter a grade for Module 4: ")))
nums.append(float(input("Enter a grade for Module 5: ")))
nums.append(float(input("Enter a grade for Module 6: ")))

# add grades entered to a list
print("\n------------Results-------------\n")
grades = nums

# TO DO: determine lowest, highest , sum and average for grades

list_min = min(grades)
print(f"Lowest Grade: {list_min}")

list_max = max(grades)
print(f"Highest Grade: {list_max}")

list_sum = sum(grades)
print(f"Sum of Grades: {list_sum}")

list_avr = sum(grades) / 6
print(f"Average:  {list_avr:.2f}")

print("------------------------------------")

# determine letter grade for average

if list_avr >= 90:
    print("Your grade is: A")

elif list_avr >= 80:
 print("Your grade is: B")

elif list_avr >= 70:
 print("Your grade is: C")

elif list_avr <= 69: 
    print("Your grade is: F")
