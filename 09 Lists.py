import random  #import the random library to use randint

def roll(die):  #define die rolling function
    intel = 0 #setting intel to 0 for all dice so it can be assigned to 1 if the die result is 0
    roll = random.randint(0, 5) #roll = a random integer from 1-6 using randint from the random library
    
    dice = { #this is a dictionary the index comes from die, and the value is counted based on the roll value
        "g": [1,1,2,0,0,0], 
        "b": [1,1,2,3,0,0],
        "a": [1,2,3,4,5,0],
        "o": [1,1,0,0,0,0]
    }

    if dice[die][roll] == 0: intel = 1 #this calld dice
    return (dice[die][roll], intel)


(groll, gintel) = roll('g') #these names don't have to match the variables from 'g' die function
(broll, bintel) = roll('b') #these names don't have to match the variables from 'b' die function
(aroll, aintel) = roll('a') #these names don't have to match the variables from 'a' die function
(oroll, ointel) = roll('o') #these names don't have to match the variables from 'o' die function
#these variables are only for use outside of the function and are populated by the tuple in the function when called


print("Alpha die result is", aroll, "and there was", aintel, "Intelligence generated")
print("Beta die result is", broll, "and there was", bintel, "Intelligence generated")
print("Gamma die result is", groll, "and there was", gintel, "Intelligence generated")
print("Objective die result is", oroll, "and there was", ointel, "Intelligence generated")


