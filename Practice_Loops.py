#loops

#For Loop using range function
...
counter = 0
for item in range(4):
    print(counter)
    counter += 2
#Outside the loop
print("The final value is", counter)    

for item in range(4):
    print (item+1)

#Here, range is 0-3 we only have a stop value
    for item in range(4):
        counter += 2
        print(counter)

#Here range is 2-9,we give a start and stop value
for num in range(2,10):
    print(num)      


stop_val = int( input("How many times do you want to run?"))
for num in range(stop_val):
    print("Program runs")
...

my_list = [2.2,6.5,8.34, 65.0]

for num in my_list:
    print(num)
...
#While loop runs until a specific condtion is met
#Create variable to control loop

run_again = "y"
while run_again == "y":
    print("\nProgram is running\n")
    run_again = input("Would you like to run program again? y or n ")
#At this point, loop has been broken
print("Program has ended, goodbye!")    
        
#Create incrementer variable
my_num = 0
#How many times the loop executes
num_loops = 0

while run_again != "no":
    #increment num_loops
    num_loops += 1

    integer = int(input("give me a number:"))
    my_num += integer

    #Control the loop - without it, its in an infinite loop
    run_again = input("Would you like to run again?")

#Break the loop
print(f"The loop ran {num_loops} times") 
print(f"The sum of the value of the loops is")   