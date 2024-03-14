#Branching - if, elif, else

num = 10
...
#if/else statement 
if num > 5:
    print("Greater than 5")
else:
    print("Less than or equal to 5") 

#If num is EQUAL to 5
if num == 5:
    print("Num is 5")    
else:
    print("Num is not 5")   

#If num is NOT EQUAL to 5
if num != 5:
    print(f"Numn is NOT 5, it is {num}")    
else: 
    print("num is 5")    
...

name = "Bob"
age = 50

if name == "Bob":
    print("Hi, Bob")
    if age > 35:
        print("Wow, your're a little old")
    else:
        print("You're a youngin")    
else:
    print("You're not Bob!")


