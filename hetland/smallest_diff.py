#Find the two closest numbers (i.e. those with the smallest absolute difference) in a list

from random import randrange

seq = [randrange(10**10) for i in range(100)]
dd = float("inf")

#Brute force method - two nested loops
for x in seq:
    for y in seq:
        if x == y: continue
        d = abs(x - y)
        if d < dd:
            xx, yy, dd = x, y, d
print (xx, yy)

seq.sort()
for i in range(len(seq)-1):
    x, y = seq[i], seq[i+1]
    if x == y: continue
    d = abs(x - y)
    if d < dd:
       xx, yy, dd = x, y, d
print (xx, yy)
