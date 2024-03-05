#List

#creates an empty list
nums = []

#Add values to the list - "hard code"
nums.append(5)
nums.append(5.758)
nums.append(63.0)
print(nums)

num1 = float(input("Enter a float value: "))

#Add variable to list
nums.append(nums)
nums.append(float(input("Enter a float value: ")))
print(nums)

#Get the sum of all values in the list
list_sum = sum(nums)
print(f"The sum of the list is: {list_sum}")

print(sum([1,1,1,1,1,1]))

#Get the minimum value from the list

list_min = min(nums)
print(f"The smallest value in the list is: {list_min}")

list_max = max(nums)
print(f"The largest value in the list is: {list_max}")

#Get the length of the list

list_length = len(nums)
print(f"The list has {list_length} items")

#Get the average of all the grades on the list

list_avr = sum(nums) / 6
print(f"Average: " {list_avr})
