#create & populate dictionary 'ages' with name & age
ages = {'julian': 20, 'bob': 23, 'zack': 3, 'anthony': 95, 'daniel': 41}
#create a list 'num' out of the dictionary set to be sorted by age
#which is the value of the key value pair
num = dict(sorted(ages.items(), key=lambda x: x[1]))
#create a list 'alpha' out of the dictionary set to be sorted by name
#which is the key of the key value pair
alpha = dict(sorted(ages.items(), key=lambda x: x[0]))
#we are creating a dictionary, creating an ordered list from that dictionary,
#then creating a new dictionary from that ordered list and printing it
for k, v in num.items():
    print(k, v)
print(' ')
for k, v in alpha.items():
    print(k, v)