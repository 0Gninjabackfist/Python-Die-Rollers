import random  #import the random library to use randint

def gdie():  #define the D6 function as gdie (gamma die)
    dieroll = random.randint(1, 6) #dieroll = a random integer from 1-6 using randint from the random libray
    if dieroll == 1: dieroll = 1
    if dieroll == 2: dieroll = 1
    if dieroll == 3: dieroll = 2
    if dieroll == 4: dieroll = 0
    if dieroll == 5: dieroll = 0
    if dieroll == 6: dieroll = 0
    #return dieroll  # this would return the dieroll value
    print(dieroll) #this tells the function to print the result of the die roll when called
gdie() #invoke the gdie function
