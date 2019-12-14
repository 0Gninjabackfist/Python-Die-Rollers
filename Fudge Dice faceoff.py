import random
#attacking fudge dice
AD61 = random.randint(1, 6)
if AD61 == 1 or AD61 == 2: AD61 = -1
if AD61 == 3 or AD61 == 4: AD61 = 0
if AD61 == 5 or AD61 == 6: AD61 = 1
AD62 = random.randint(1, 6)
if AD62 == 1 or AD62 == 2: AD62 = -1
if AD62 == 3 or AD62 == 4: AD62 = 0
if AD62 == 5 or AD62 == 6: AD62 = 1
AD63 = random.randint(1, 6)
if AD63 == 1 or AD63 == 2: AD63 = -1
if AD63 == 3 or AD63 == 4: AD63 = 0
if AD63 == 5 or AD63 == 6: AD63 = 1
AD64 = random.randint(1, 6)
if AD64 == 1 or AD64 == 2: AD64 = -1
if AD64 == 3 or AD64 == 4: AD64 = 0
if AD64 == 5 or AD64 == 6: AD64 = 1
#defending fudge dice
DD61 = random.randint(1, 6)
if DD61 == 1 or DD61 == 2: DD61 = -1
if DD61 == 3 or DD61 == 4: DD61 = 0
if DD61 == 5 or DD61 == 6: DD61 = 1
DD62 = random.randint(1, 6)
if DD62 == 1 or DD62 == 2: DD62 = -1
if DD62 == 3 or DD62 == 4: DD62 = 0
if DD62 == 5 or DD62 == 6: DD62 = 1
DD63 = random.randint(1, 6)
if DD63 == 1 or DD63 == 2: DD63 = -1
if DD63 == 3 or DD63 == 4: DD63 = 0
if DD63 == 5 or DD63 == 6: DD63 = 1
DD64 = random.randint(1, 6)
if DD64 == 1 or DD64 == 2: DD64 = -1
if DD64 == 3 or DD64 == 4: DD64 = 0
if DD64 == 5 or DD64 == 6: DD64 = 1
#roll each die and save totals
aroll = AD61 + AD62 + AD63 + AD64
droll = DD61 + DD62 + DD63 + DD64
#print the 2 rolls
print(aroll,',',droll)
#conditional print based on results
if aroll > droll: 
    print('attacker wins by',aroll-droll)
if aroll < droll: 
    print('defender wins by',droll-aroll)
if aroll == droll: 
    print ('tie')
