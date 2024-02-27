
item1 = input("enter the first item ")
price1 = float(input("how much is the "+ item1))

item2 = input("enter the second item ")
price2 = float(input("how much is the "+ item2))

item3 = input("enter the third item ")
price3 = float(input("how much is the "+ item3))

subtotal = price1 + price2 + price3
print(subtotal)

tax_rate = float(input("Enter the tax percentage without %: "))
tax_rate = tax_rate/100
tax_amount = subtotal * tax_rate
print("Subtotal:", subtotal)
print("Tax:", format(tax_amount, ".2f"))
print("Total:", format(subtotal + tax_amount, ".2f"))



