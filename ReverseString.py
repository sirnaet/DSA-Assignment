#Reverse a string without using [::-1]
def reverse_string(s):
    reversed_str = '' #Empty string
    for char in s: #Iterate through each character in the string
        reversed_str = char + reversed_str #Add the character to the front of the string
    return reversed_str  #return the reversed string

print(reverse_string("Brian")) #testing the function