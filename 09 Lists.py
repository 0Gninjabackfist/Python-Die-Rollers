import random  #import the random library to use randint

def roll(die):  #define the D6 function as gdie (gamma die)
    intel = 0 #setting intel to 0 for all dice so it can be assigned to 1 if the die result is 0
    roll = random.randint(0, 5) #roll = a random integer from 1-6 using randint from the random library
    gdie = [1,1,2,0,0,0]
    bdie = [1,1,2,3,0,0]
    adie = [1,2,3,4,5,0]
    odie = [1,1,0,0,0,0]
    if die == 'g':
        if gdie[roll] == 0: intel = 1 #this assignes intel to 1 if the die rolls a 0, it's default a 0 itself
        return (gdie[roll], intel)
    if die == 'b':
        if bdie[roll] == 0: intel = 1 #this assignes intel to 1 if the die rolls a 0, it's default a 0 itself
        return (bdie[roll], intel)
    if die == 'a':
        if adie[roll] == 0: intel = 1 #this assignes intel to 1 if the die rolls a 0, it's default a 0 itself
        return (adie[roll], intel)
    if die == 'o':
        if odie[roll] == 0: intel = 1 #this assignes intel to 1 if the die rolls a 0, it's default a 0 itself
        return (odie[roll], intel)

(groll, gintel) = roll('g') #these names don't have to match the variables from 'g' die function
(broll, bintel) = roll('b') #these names don't have to match the variables from 'b' die function
(aroll, aintel) = roll('a') #these names don't have to match the variables from 'a' die function
(oroll, ointel) = roll('o') #these names don't have to match the variables from 'o' die function
#these variables are only for use outside of the function and are populated by the tuple in the function when called


print("Alpha die result is", aroll, "and there was", aintel, "Intelligence generated")
print("Beta die result is", broll, "and there was", bintel, "Intelligence generated")
print("Gamma die result is", groll, "and there was", gintel, "Intelligence generated")
print("Objective die result is", oroll, "and there was", ointel, "Intelligence generated")


