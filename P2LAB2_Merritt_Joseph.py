#Joseph_Merritt
#27_Feb_24
#P2LAB2 - Math Expressions and F-String

#Get input from user
num1 = float(input("Enter a float: "))
num2 = float(input("Enter a float: "))
num3 = float(input("Enter a float: "))
num4 = float(input("Enter a float: "))

#Calculate the product of variables
product = num1 * num2 * num3 * num4

#Calculate the average
average = (num1 + num2 + num3 + num4) / 4

#Display info to user
print(f"The product is: {product:.0f}")
print(f"The average is: {average:.0f}")

print(f"The product is: {product:.3f}")
print(f"The average is: {average:.3f}")

