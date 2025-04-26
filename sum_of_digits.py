#Returns sum of all digits of a number
def sum_of_digits(i): #Define a function that takes an integer as an argument
    total = 0 #Start with a total of 0
    while i > 0: #While the number is greater than 0
        digit = i % 10 #Get the last digit of the number
        total += digit #Add the digit to the total
        i = i // 10 #Remove the last digit from the number
    return total #Return the final total

print(sum_of_digits(1234)) #testing the function