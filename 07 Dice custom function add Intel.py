import random  #import the random library to use randint

def roll(die):  #define the D6 function as gdie (gamma die)
    if die == 'g':
        groll = random.randint(1, 6) #groll = a random integer from 1-6 using randint from the random library
        if groll == 1: groll = 1
        if groll == 2: groll = 1
        if groll == 3: groll = 2
        if groll == 4: groll = 0
        if groll == 5: groll = 0
        if groll == 6: groll = 0
        if groll == 0: intel = 1 #<<how is this going to work?
        return groll, intel #<<how is this going to work?
    if die == 'b':
        broll = random.randint(1, 6) #broll = a random integer from 1-6 using randint from the random library
        if broll == 1: broll = 1
        if broll == 2: broll = 1
        if broll == 3: broll = 2
        if broll == 4: broll = 3
        if broll == 5: broll = 0
        if broll == 6: broll = 0
        return broll
        #print('beta die rolls:',(broll)) #this tells the function to print the result of the die roll when called
    if die == 'a':
        aroll = random.randint(1, 6) #aroll = a random integer from 1-6 using randint from the random library
        if aroll == 1: aroll = 1
        if aroll == 2: aroll = 2
        if aroll == 3: aroll = 3
        if aroll == 4: aroll = 4
        if aroll == 5: aroll = 5
        if aroll == 6: aroll = 0
        return aroll
    if die == 'o':
        oroll = random.randint(1, 6) #oroll = a random integer from 1-6 using randint from the random library
        if oroll == 1: oroll = 1
        if oroll == 2: oroll = 1
        if oroll == 3: oroll = 0
        if oroll == 4: oroll = 0
        if oroll == 5: oroll = 0
        if oroll == 6: oroll = 0
        return oroll


print("Alpha die rolled a ", roll('a')) #invoke the die function for 'a' gamma die
print("Beta die rolled a ", roll('b')) #invoke the die function for 'b' gamma die
print("Gamma die rolled a ", roll('g')) #invoke the die function for 'g' gamma die
print("Objective die rolled a ", roll('o')) #invoke the die function for 'g' gamma die

