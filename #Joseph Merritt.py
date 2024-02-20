#Joseph Merritt
#20 February 2024
#Program Detail - Input/Output


#Street is a string datatype
street = ("What is your street?")

#convert to int() in the same line
house_num = int(input("What is your house number"))

#convert to int() seperately
house_num = int(house_num)

#Calculate neighbor's house number

neb_num = int(house_num + 2)

#Print our address & neighbor address

print("Your address is",house_num, street)
print("Your neighbor's address is", neb_num, street)

