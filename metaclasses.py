'''
Introduction to METACLASSES in Python

Consider an example: we have a bunch of 'Philosopher' classes, each of which needs the same 'set' of methods ('the_answer()') as the
basics for his pondering and brooding. A naive solution would be to implement the classes as having the same function the_answer()
in each philosopher class.

Another flawed implementation, which at least avoids creating redundant code, consists in designing a base class which contains
'the_answer()' as a method, and each philosopher class inherits now from this base class
'''

class Answer:
    def the_answer(self, *args):
        return 42

class Philosopher1(Answer):
    pass

class Philosopher2(Answer):
    pass

plato = Philosopher1()
aristotle = Philosopher2()
print plato.the_answer(), aristotle.the_answer()

'''
In the above, each Philosopher class will always have a method "the_answer". If we don't know a priori that we want or need this
method, then we can use a decision to decide whether a class needs to be augmented with a function at runtime
'''

def the_answer(self, *args):
    return 42

class Philosopher3:
    pass

required = True
if required:
    Philosopher3.the_answer = the_answer

kant = Philosopher3()
try: print kant.the_answer()
except NameError: print "Kant doesn't have the answer"

'''
This approach is still insufficient because we have to add the same code to every class and may be awkward if there are many
methods that we want to add. We could use a manager function to augment the classes conditionally, and use a decorator to ensure
that we don't forget to call the manager function if it is needed...
'''

required = True

def another_answer(self, *args):
    return "I have the answer!"

def augment_answer(cls):
    if required:
        cls.the_answer = another_answer
    return cls

@augment_answer
class Philosopher4:
    pass

socrates = Philosopher4()
print socrates.the_answer()

'''
The above is a good answer, but a better answer is to use METACLASSES.
A METACLASS is a class whose instances aare classes. Like an 'ordinary' class defines the behaviour of the instances of the class,
a metaclass defines the behaviour of classes and their instances. Uses for metaclasses include registering classes at creation
time, automatically adding new methods and automatic property creation.

Principally, metaclasses are defined like any other Python class, but they are classes that inherit from 'type'. Another difference
is that a metaclass is defined automatically, when the class statement using a metaclass ends. i.e. if no 'metaclass' keyword
is passed after any base classes of the class header, type() (i.e. __call__ of type) will be called. If a metaclass keyword is
used on the other hand, the class assigned to it will be called instead of type.

A simple metaclass:

N.B. the Python 3 Syntax is:
class A(S, metaclass=LittleMeta):
    pass
'''

class LittleMeta(type):
    def __new__(cls, clsname, superclasses, attributedict):
        print "clsname:", clsname
        print "superclasses:", superclasses
        print "attributedict:", attributedict
        return type.__new__(cls, clsname, superclasses, attributedict)

class S(object):
    pass

class A(S):
    __metaclass__ = LittleMeta

a = A()

'''
The metaclass LittleMeta prints the content of its arguments in the __new__ method and returns the results of the type.__new__ call
Upon instantiating th class A, we can see that LittleMeta.__new__ has been called (and not type.__new__)

Resuming our philosopher problem: we define a metaclass "EssentialAnswers" which is capable of automatically including our
augment_answer method:
'''

required = True

def yet_another_answer(self, *args):
    return "I have another answer!"

class EssentialAnswers(type):
    def __init__(cls, clsname, superclasses, attributedict):
        if required:
            cls.the_answer = yet_another_answer

class Philosopher5():
    __metaclass__ = EssentialAnswers
    pass

pythagoras = Philosopher5()
try: print pythagoras.the_answer()
except NameError: print "Pythagoras doesn't have the answer!"

'''
For an 'ordinary' class, after a class definition has been processed, Python calls
type(classname, superclasses, attributes_dict)
This is NOT the case if a metaclass has been declared in the header. In this case, the ordinary class is 'hooked' to the metaclass,
and that metaclass is called instead of type

Another example usage: creating singletons using metaclasses.
The singleton pattern is a design pattern that restricts the instantiation of a class to one object. It is used in cases where
exactly one object is needed. The concept can be generalised to restrict the instantiation to a certain number of objects.
'''

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class SingletonClass():
    __metaclass__ = Singleton
    pass

singletonclass1 = SingletonClass()
singletonclass2 = SingletonClass()
print (singletonclass1 == singletonclass2) # is True because we can only have one instantiation of the class

'''
Alternatively, we can create Singleton classes by INHERITING from a Singleton class, which can be defined like this:
Python 3 only

class Another_Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

class Another_SingletonClass(Another_Singleton):
    pass

another_singletonclass1 = Another_SingletonClass()
another_singletonclass2 = Another_SingletonClass()
print (another_singletonclass1 == another_singletonclass2) # is True because we can only have one instantiation of the class
'''
