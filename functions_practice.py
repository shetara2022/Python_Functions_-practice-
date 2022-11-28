#A function named hello() that prints a greeting to the user. This function should accept no arguments and returns nothing.
# def hello():
#     print("Hello There!")

# hello()

"""
A function named pack() that accepts three arguments, 
and returns a single list with the three arguments inside as list elements
"""
# def pack(firstname, middlename, lastname):
#     return[firstname, middlename, lastname]

# print("Martin", "Luther", "King")

"""
A function called eat_lunch(). 
This function should accept a list of any length, and print out a series of strings that say "First I eat __" (the first element of the list), 
and "Next I eat ___" (for the following elements in the list). If the list is empty, print "My lunchbox is empty!". 
The function should not return anything
"""
def eat_lunch(*list):
    if len(list) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat " + list[0])
        print("Next I eat " + list[1])
eat_lunch("burger", "turkey")
    
    