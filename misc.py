#creating a list and looping over it to make another list
index = [2*i for i in range(0,10)]

index = []
for i in range(10):
    index.append(2*i)

index = list(map(lambda i: 2*i, range(10)))

#find index of first occurence of elements in list according to order
order = [2,4,6]
index2 = [list(index).index(i) for i in order]
print index2
