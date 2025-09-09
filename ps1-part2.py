# Write a function that takes two variables and does all the computations asked
def number_fun(a,b):
    number_fun(firstnum,secondnum)
# Ask the user for the first number, store the value in a variable
firstnum=int(input("Please give me an integer between 10 and 100:"))
a= firstnum

# Ask the user for the second number, store the value in a variable
secondnum= int(input("Please enter a intenger less than 4:"))
b= secondnum

# Repeat back the numbers
print("You entered", a,"and", b)

# Perform calculations. Be careful about string formatting for autograders.
print(a+b)
print(a*b)
print(a**b)
print(a%b)
