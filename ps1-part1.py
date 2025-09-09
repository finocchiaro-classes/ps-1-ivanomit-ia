# Ask the user for the first number, store the value in a variable
firstnum= int(input('Please give me an intenger between 10 and 100:'))
a= firstnum
# Ask the user for the second number, store the value in a variable
secondnum= int(input('Please give me an other integer less than 4:'))
b=secondnum
# Repeat back the numbers
print("You entered", a,"and", b)
# Perform calculations. Be careful about string formatting for autograders.
print(a+b)
print(a*b)
print(a**b)
print(a%b)
