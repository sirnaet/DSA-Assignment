#calculates factorial using a loop
def factorial_loop(n):
    result = 1 #Start with a result of 1
    for i in range(1, n+1): #Loop from 1 to n (inclusive)
        result *=1 #Multiply the result by i
    return result #Return the final result

print(factorial_loop(5)) #testing the function