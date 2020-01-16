import random  #import the random library to use randint

####################################################################################################################################################
#this is a dictionary the index comes from die, and the value is counted based on the roll value
dice = { 
    "g": [1,1,2,0,0,0], 
    "b": [1,1,2,3,0,0],
    "a": [1,2,3,4,5,0],
    "o": [1,1,0,0,0,0]
}
####################################################################################################################################################

def roll(die,sides):  #define die rolling function, 1 parameters die (what are the die face values) and sides (how many sides does the die have)
    face = random.randint(0, sides-1) #roll = a random integer from 1-6 using randint from the random library
    


    value = die[face] # creates a variable that returns the value of the die of that type on that face
    return (value, face) #the face here is if later i need to know which side of the die was roll 0-5


####################################################################################################################################################
   
#this adds the result of a series of dice from a list defined up in 'dice'
attdice = ['g','g','b']
attroll = 0  #set the attroll variable to zero so we can increment it
for adie in attdice: #for each value in the attdice list we are going to do the below
    (aresult,_) = roll(dice[adie],6) #we ask for the value from the 3 part roll function return, ignoring the 2nd and 3rd value
    attroll = attroll + int(aresult) #adding up the total of the die values
print('Attacker total =', attroll) #print out the total of the values rolled
    
####################################################################################################################################################


# (groll,gface) = roll(dice['g'],6) #these names don't have to match the variables from 'g' die function, the underscore is telling it to ignore
# (broll,bface) = roll(dice['b'],6) 
# (aroll,aface) = roll(dice['a'],6) 
# (oroll,oface) = roll(dice['o'],6)
# # #these variables are only for use outside of the function and are populated by the values in the function when called


# print("Alpha die result is", aroll)
# print("Beta die result is", broll)
# print("Gamma die result is", groll)
# print("Objective die result is", oroll)