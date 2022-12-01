
#Write a Python function called max_num()to find the maximum of three numbers
def max_num(x, y, z):
    return max([x,y,z])

print(max(100, 5, 37))

#Write a Python function called mult_list() to multiply all the numbers in a list
def mult_list(list): 
    # Product = 1 to multiply first numnber in the list to get back that number
    product = 1
    #loop through each factor in the list and multiply by product
    for factor in list:
        product = product * factor
    return product

list1 = [2, 3, 4, 7]
print(mult_list(list1))   

#Write a Python function called rev_string() to reverse a string.
def rev_string(my_name):
    return my_name[::-1]

name = rev_string("Shetara Smith")
print(name)

#Write a Python function called num_within() to check whether a number falls in a given range
def num_within(d, e, f):
    return d in range (e, f+1)
    
print(num_within(7,8,9))
