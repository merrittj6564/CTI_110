#User-defined functions

#Define a function

def multiply(a, b):
    print(f"Multiply {a} ande {b}")
    result = a * b
    return result

#Call the function
answer = multiply(2, 6)
print(answer)

'''
def hello(string1, string2, string3):
    print(f"The first parameter is {string1}")
    print(f"The second parameter is {string2}")
    print(f"The third parameter is {string3}")
hello("Dog", "Cat", "Mouse")

def add(a, b, c):
    print(f"add {a}, {b}, {c}")
    result = a + b + c
    return result
returned_value = add(3, 4, 5)
print(returned_value)
'''