import numpy as np

a = [1.0, 0.0, 2.0, 1.0, 1.0, 0.0, 1.0]
b = [1.0, 0.0, 1.0, 0.5, 1.0, 0.0, 1.0]

x1 = np.dot(a,b)
print 'dot product =', x1

n = len(a)

c = a[:]
print c

#avoid an index (say, 4th element)
x2 = np.dot(a[0:3],b[0:3]) + np.dot(a[4:7],b[4:7])
print 'dot product with missing element =', x2

#matrix multiplication
d = np.array([[1,0], [0,1]])
e = np.array([[4,1], [2,2]])
f = np.zeros((2,2))
for i in range(0,2):
    for j in range(0,2):
        f[i,j] = np.dot(d[i,:],e[:,j])
print f
#is equivalent to...
g = np.dot(d,e)
print g
