#Calculates factorial using recursion
def factorial_recursive(j):
    if j == 0 or j == 1: #Base case: if j is 0 or 1, return 1
        return 1 
    else: #Recursive case: multiply j by the factorial of (j-1)
        return j * factorial_recursive(j-1)
    
print(factorial_recursive(5)) #testing the function