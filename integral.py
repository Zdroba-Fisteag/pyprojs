import math

# Very simple function for the indefinite integral (WIP)
def indefint():
    x = int(input("Input a base number (x): "))
    n = int(input("Input an exponent number (n): "))
    print(x, " ", n)
    y = (x**(n+1))/(n+1) , "+ c" # Added the "+c for the indefinite integral"
    print(y)

def defint():
    print("We won't be needing a number 'x', as the definite integral is calculated based on the bounds.")
    # x = int(input("Input a base number: ")) not needed
    a = int(input("Input your lower limit/bound (a): "))
    b = int(input("Input your upper limit/bound (b): "))
    n = int(input("Input an exponent number (n): "))
    y = (b**(n+1))/(n+1) - (a**(n+1))/(n+1) # = [(x**(n+1))/(n+1)]_a^b
    print(y)

print("Type 'i' for indefinite or 'd' for definite integral")
inp = input("Input what kind of integral you'd like solved:")
if(inp == 'i'):
    indefint()
elif(inp == 'd'):
    defint()
else:
    print("Operation cancelled by default")
    pass

# Running some test functions to get myself further into this:

