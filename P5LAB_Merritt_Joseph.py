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

def add_items(dictionary):
    cart = []
    choice = input("Enter an item to add to the cart or type 'end' to stop:")
    while choice != "end":
        if choice in dictionary.keys():
            cart.append(choice)
        else: 
            print(f"{choice} is not in stock")
        choice = input("Enter an item to add to the cart or type 'end' to stop:")
    return cart          

def calc_totals(cart, dictionary):
    print("Grocery Receipt")
    print("----------------------------")
    print()
    subtotal = 0
    for item in cart:
        print(f"{item:<20} ${dictionary[item]:.2f}")
        subtotal += dictionary[item]
    tax = subtotal * .07
    final_total = tax + subtotal
    print()
    print(f"SUBTOTAL:          {subtotal:.2f}")
    print()
    print(f"TAX:          {tax:.2f}")
    print(f"TOTAL:          {final_total:.2f}")
    return subtotal, tax, final_total




#Main Function
def main():
    food_dictionary = {"apples":3.69, "berries":4.00, "chocolate":2.89, "turkey":6.99, "cheese":4.00, "pepsi":7.89, "eggs":3.50, "bread":3.00}
    show_avail_items(food_dictionary)

    cart = add_items(food_dictionary)
    print("Items in your cart:")
    for item in cart:
        print(item)

    subtotal, tax, final_total = calc_totals(cart, food_dictionary)
    print(subtotal)
    print(tax)
    print(final_total)


#Call the Main Function
main()         