import random

distribution = dict()
n=10000
while n > 0:
    D61 = random.randint(1, 6)
    if D61 == 1 or D61 == 2: D61 = 0
    if D61 == 3 or D61 == 4: D61 = 1
    if D61 == 5 or D61 == 6: D61 = 2
    D62 = random.randint(1, 6)
    if D62 == 1 or D62 == 2: D62 = 0
    if D62 == 3 or D62 == 4: D62 = 1
    if D62 == 5 or D62 == 6: D62 = 2
    D63 = random.randint(1, 6)
    if D63 == 1 or D63 == 2: D63 = -1
    if D63 == 3 or D63 == 4: D63 = 0
    if D63 == 5 or D63 == 6: D63 = 1
    D64 = random.randint(1, 6)
    if D64 == 1 or D64 == 2: D64 = -1
    if D64 == 3 or D64 == 4: D64 = 0
    if D64 == 5 or D64 == 6: D64 = 1
    
    roll = D61 + D62 + D63 + D64
    distribution[roll] = distribution.get(roll,0) + 1
    n = n - 1
for key in sorted(distribution.keys()):
    print("%s: %s" % (key, distribution[key]))
