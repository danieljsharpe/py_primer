#Examples on using classes

import numpy as np

class F:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.A = 1.0

    def value(self,x):
        return self.A*np.exp(-(self.p1*x)+self.p2)

    def formula(self):
        return 'A*exp(-(p1*x)+p2); A,p1,p2 = %g, %g, %g ' \
               % (self.A, self.p1, self.p2)

#instantiate class
f = F(0.1,0.5)
#print parameters
print "parameters are:", f.p1, f.p2, f.A
#call value function
y = f.value(1.0)
#call function that returns string and print
print f.formula()
#create second instance of class with new parameters p1 & p2
f2 = F(0.2,0.8)
print f.value(1.0), f2.value(1.0)

#use instances in a user-defined function
def diff(f, x, h=1E-5):
    return (f(x+h) - f(x))/h

df1dt = diff(f.value, 0.1)
df2dt = diff(f2.value, 0.1)
print df1dt, df2dt

#here, inside the diff function, the argument f now behaves as a function of one variable
#that automatically carries with it 3 variables (p1,p2,A). When f refers to (e.g.)
#f2.value, Python knows that f(x) means f2.value(x), and inside the f2.value method
#self is f2, and we have access to f2.p1 etc.
