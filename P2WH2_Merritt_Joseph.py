#Joseph Merritt
#5 March 2024
#P2WH2
#Grade List - Creating Lists

#creates an empty list
nums = []

#Add variable to list

nums.append(float(input("Enter a grade for Module 1: ")))
nums.append(float(input("Enter a grade for Module 2: ")))
nums.append(float(input("Enter a grade for Module 3: ")))
nums.append(float(input("Enter a grade for Module 4: ")))
nums.append(float(input("Enter a grade for Module 5: ")))
nums.append(float(input("Enter a grade for Module 6: ")))

print("\n------------Results-------------\n")

#Get the minimum grade from the list

list_min = min(nums)
print(f"Lowest Grade: {list_min}")

#Get the maximum grade from the list

list_max = max(nums)
print(f"Highest Grade: {list_max}")

#Get the sum of all grades in the list

list_sum = sum(nums)
print(f"Sum of Grades: {list_sum}")

#Get the average of all the grades on the list

list_avr = sum(nums) / 6
print(f"Average:  {list_avr:.2f}")
print("------------------------------------")

