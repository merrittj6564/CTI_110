#Joseph_Merritt
#11_Apr_24
#P5LAB - User Defined Functions

#Function to determine change returned to customer
def disperse_change(change):
    if change == 0:
        print("No Change Due")

#Calculate the amount of each coin needed
#integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

#Display coins owed

    if num_dollars > 0:
        print(num_dollars,  end=" ")
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
            
    if num_quarters > 0:
        print(num_quarters,  end=" ")
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")

    if num_dimes > 0:
        print(num_dimes,  end=" ")
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")

    if num_nickles > 0:
        print(num_nickles,  end=" ")
        if num_nickles == 1:
            print("Nickle")
        else:
            print("Nickles")

    if num_pennies > 0:
        print(num_pennies,  end=" ")
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")

def show_avail_items(dictionary):
    print(f"{'Grocery Items':<15}{'Price'}")
    print("--------------------------------------")
    for key, value in dictionary.items():
        print(f"{key:<15}${value:.2f}")
    print("--------------------------------------")    

#Main Function
def main():
    food_dictionary = {"apples":3.69, "berries":4.00, "chocolate":2.89}
    show_avail_items(food_dictionary)        