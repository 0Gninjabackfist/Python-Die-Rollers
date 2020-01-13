import random  #import the random library to use randint

####################################################################################################################################################

dice = { #this is a dictionary the index comes from die, and the value is counted based on the roll value
    "g": [1,1,2,0,0,0], 
    "b": [1,1,2,3,0,0],
    "a": [1,2,3,4,5,0],
    "o": [1,1,0,0,0,0]
}
####################################################################################################################################################

def roll(die,sides):  #define die rolling function
    intel = 0 #setting intel to 0 for all dice so it can be assigned to 1 if the die result is 0
    face = random.randint(0, sides-1) #roll = a random integer from 1-6 using randint from the random library
    


    value = die[face] # creates a variable that returns the value of the die of that type on that face
    if value == 0: intel = 1 #this sets to the Intel to 1 if a blank was rolled
    return (value, intel, face) 
    #the face here is if later i need to know which side of the die was roll 0-5


####################################################################################################################################################
   
#this adds the result of a series of dice from a list defined up in 'dice'
attdice = ['g','g','b']
attroll = 0
for adie in attdice:
    (aresult,_,_) = roll(dice[adie],6)
    attroll = attroll + int(aresult)
print('Attacker total =', attroll)
    
####################################################################################################################################################


# (groll, gintel, _) = roll(dice['g'],6) #these names don't have to match the variables from 'g' die function, the underscore is telling it to ignore
# (broll, bintel, _) = roll(dice['b'],6) 
# (aroll, aintel, _) = roll(dice['a'],6) 
# (oroll, ointel, _) = roll(dice['o'],6)
# #these variables are only for use outside of the function and are populated by the values in the function when called


# print("Alpha die result is", aroll, "and there was", aintel, "Intelligence generated")
# print("Beta die result is", broll, "and there was", bintel, "Intelligence generated")
# print("Gamma die result is", groll, "and there was", gintel, "Intelligence generated")
# print("Objective die result is", oroll, "and there was", ointel, "Intelligence generated")