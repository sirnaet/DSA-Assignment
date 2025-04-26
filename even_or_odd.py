#Checks whether a no. is even or odd
def even_or_odd(l): 
    if l % 2 == 0: #If the no. is divisible by 2, it is even
        return "Even" 
    else: #If the no. is not divisible by 2, it is odd
        return "Odd"
    
print(even_or_odd(7)) #testing the function