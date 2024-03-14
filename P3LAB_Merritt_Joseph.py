#Joseph Merritt
#3/14/2024
#P3LAB - Branching

#Get amount of changed owed from user
change = int(input("Enter an amount of change as integer: "))

#Calculate the amount of each coin needed
#integer division - //

num_dollars = change // 100
change = change - (num_dollars * 100)