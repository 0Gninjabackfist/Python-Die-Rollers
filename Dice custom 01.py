#bring in the random item from the library
import random
#create a dictionary called 'distribution'
distribution = dict()
#set the number of rolls to 10000
n=10000
#set the while countdown to stop when n = 0
while n > 0:
    #set each 6 sided die with values for each side from 0 to 2 (4 Betralyal dice)
    D61 = random.randint(1, 6)
    if D61 == 1: D61 = 0
    if D61 == 2: D61 = 0
    if D61 == 3: D61 = 1
    if D61 == 4: D61 = 1
    if D61 == 5: D61 = 2
    if D61 == 6: D61 = 2
    D62 = random.randint(1, 6)
    if D62 == 1: D62 = 0
    if D62 == 2: D62 = 0
    if D62 == 3: D62 = 1
    if D62 == 4: D62 = 1
    if D62 == 5: D62 = 2
    if D62 == 6: D62 = 2
    D63 = random.randint(1, 6)
    if D63 == 1: D63 = 0
    if D63 == 2: D63 = 0
    if D63 == 3: D63 = 1
    if D63 == 4: D63 = 1
    if D63 == 5: D63 = 2
    if D63 == 6: D63 = 2
    D64 = random.randint(1, 6)
    if D64 == 1: D64 = 0
    if D64 == 2: D64 = 0
    if D64 == 3: D64 = 1
    if D64 == 4: D64 = 1
    if D64 == 5: D64 = 2
    if D64 == 6: D64 = 2
    #roll is set to be the sum of 1 roll of each of the 4 dice
    roll = D61 + D62 + D63 + D64
    #add the total 'roll' to the dictionary 'distribution' with roll total and count of that total
    distribution[roll] = distribution.get(roll,0) + 1
    #subtract 1 from N as we count down to the number of rolls
    n = n - 1
#print the dictionary
for k,v in distribution.items():
    print(k, v)
