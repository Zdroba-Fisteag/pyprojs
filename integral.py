import math

# Very simple function for the indefinite integral (WIP)
def indefint():
    # x = int(input("Input a base number (x): "))
    # n = int(input("Input an exponent number (n): "))
    l = int(input("Input the amount of terms you would like to have (int): "))
    # print(x, " ", n)
    for i in range(l):
        yr = []
        x = int(input("Input a base number for this part of the term (x): "))
        n = int(input("Input an exponent number for this term (n): "))
        y = float((x**(n+1))/(n+1))
        yr.append(y)
        ys = yr[i]
        if len(yr) > i:
            print(ys)
        else:
            SyntaxWarning("You have somehow surpassed the index barrier")
        i += 1
    # print(y)

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

# ha = 5
# i = 0
# for i in range(ha):
#     i = i/2
#     i += 1
#     print(i)