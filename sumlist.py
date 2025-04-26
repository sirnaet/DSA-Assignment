#Adds all elements in a list
def sum_list(mylist): #Define a function that takes a list as an argument
    total = 0      #Start with a total of 0
    for item in mylist:
        total += item
    return total

print(sum_list([1,2,3,4,5])) #testing the function