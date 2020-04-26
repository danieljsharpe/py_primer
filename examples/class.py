import numpy as np

'''class: pack together a set of data (variables) with a set of functions operating on the
data. Achieve more modular code in this way.'''

'''
example 1: function with parameters as well as variables
consider:  f(x;p1,p2,...,pn,A)
we want to write a function f(x) i.e. depending ONLY on the indep variable argument
and NOT the parameters {p} or the fixed parameter A

A BAD solution:'''

def f(x):
    A = 1.0
    return A*np.exp(-(p1*x)+p2)

p1 = 0.1
p2 = 0.5; r1 = f(x=1.0)
p2 = 0.8; r2 = f(x=1.0)

'''works only if p is a globally defined variable initialised before the function f
is called. Problematic if we need to work with several versions of a function (here with
different values of p2, which must be set prior to the call). Other parts of the program
may alter p2 and thus alter the correctness of the function f.

A GOOD solution: implement a class!
-set of variables and set of functions held together as a single unit
-variables are visible in ALL the functions in the class, but NOT outside the class
These points are also true of modules, but classes have additional characteristics:
-most importantly: one can make copies of a class

In the class solution to this problem:
-the parameters p1, p2 & A constitute the 'data'
-the function, say value(x), used to compute the value of f(x;p1,p2,A), needs access to the data
-the class must have another function, the so-called constructor, for initialising the data.
In python, the constructor is always called __init__, which must take an argument self
-conventionally class names start with a capital letter'''

class F:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        self.A = 1.0

    def value(self,x):
        return self.A*np.exp(-(self.p1*x)+self.p2)

f = F(0.1,0.5)
print "parameters are:", f.p1, f.p2, f.A
y = f.value(1.0)

'''What has happened here?
-the class has created a new data type (of name F), and we have used the class to make an
object f whose type is F^2. An object of a user-defined class is an INSTANCE. Instantiating a
class allows us to use the data in the class and call the value function
-seemingly, we call the class F as if it were a function. In actuality, F(...) is automatically
translated by Python to call the constructor __init__ in class F. The arguments in the call are
always passed on as arguments to __init__ after the self argument. It is a rule that the self
argument is never used in calls to functions in classes
-to access functions and variables in a class, we must prefix the function and variable names by the
instance (here f) followed by a dot.

Overview of terminology:
-instance: object of a class
-method: function contained within a class
-attribute: variable (data) in a class
-constructor: function for initialising the data. Is automatically called when we create new instances

More on the self variable:
Inside the constructor __init__, the argument self is a variable holding the new instance to be
constructed, and is used to define attributes. The self parameter is invisibly returned to the
calling code. i.e. we can imagine that Python translates the instantiation code thusly:
f = F(0.1,0.5) --> F.__init__(f,0.1,0.5)
so that when we do self.p1=p1 in the constructor, we actually initialise f.p1
Here the notation for reaching a class method; F.value
is in analogy to reaching a function within a module; mod.func
Note that if we prefix with F., we need to explicitly feed in an instance f for the self argument,
but if we prefix with the instance name f., then the self argument is dropped.
Once we have instantiated the class F, the instance f 'becomes' self.

Overview of the rules regarding the "self" variable:
-any class method must have self as first argument
-self represents an (arbitrary) instant of a class
-to access another class method or a class attribute "name", inside class methods we must prefix with
self, i.e. use "self.name"
-self is dropped as argument in calls to class methods

Remark: A common mistake is to place the code that applies the class at the same
indentation as the class methods. This is illegal. Only method definitions and
assignments to so-called static attributes can appear in the indented block under
the class headline. Ordinary attribute assignment must be done inside methods. The
main program using the class must appear with the same indent as the class headline.
'''


