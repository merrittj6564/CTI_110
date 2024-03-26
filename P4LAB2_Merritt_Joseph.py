#Joseph_Merritt
#26_Mar_24
#P4LAB2 - Using the range function

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

#While loop - as long as num1 is smaller than num2, increase by 5 each

while num1 > num2: #Bad
    print("First number must be smaller")
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
#Code will happen ONLY when the loop breaks
print("You did it right!")    
        