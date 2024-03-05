#Joseph Merritt
#5 March 2024
#P2WH1
#Edit and Enhance Exiting Programs

print("This program calculates and displays travel expenses")

budget = float(input("What is your budget? "))
travel_des = input("What is your travel destination: ")
gas = float(input("How much do you think you will spend in gas? "))
accom = float(input("Approximately, how much will you need for accomadation/hotel? "))
food = float(input("Last, how much do you need for food? "))

print("\n----------Travel Expenses------------")

print("Location: ", travel_des)
print("Initial Budget: ", budget)
print("Fuel: ", gas)
print("Accomodation: ", accom)
print("Food: ", food)
expenses = gas + accom + food
print("----------------------------------------\n")
print("Remaining Balance: ", budget - expenses)
