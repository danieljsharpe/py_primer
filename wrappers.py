'''
Python examples to illustrate the use of function wrappers and decorators
'''

'''
A DECORATOR PATTERN is a way of apparently modifying an object's behaviour by enclosing it inside a decorating object
with a similar interface
'''


'''
A PYTHON DECORATOR allows us to conveniently alter functions (incl methods / functions in classes). 
Example: suppose that you would like to do something at the entry and exit points of a function, such as checking pre-
and post-conditions. FUNCTION DECORATOR Example: the decorator (@adecorator) is applied to a function definition
by placing it on the line immediately preceding the function definition. The decoration mechanism can be either a
class or a function. When the compiler passes over the code, afunction() is compiled and the resulting function
object is passed to the adecorator code, which does something to produce a function-like object that is then
substituted for the original afunction(). Note that the only constraint upon the object returned by the decorator
is that it can be used as a function, i.e. it must be callable. Thus any classes that we use as decorators must
implement __call__
'''

class adecorator(object):

    def __init__(self, func):
        self.func = func

    def __call__(self):
        print "Do something before %s is properly called..." % self.func.__name__
        self.func()
        print "Do something before %s is properly exited..." % self.func.__name__
        return

@adecorator
def afunction1():
    print "Inside afunction1()"

@adecorator
def afunction2():
    pass

afunction1()
afunction2()

'''
In the above, note that the constructor for adecorator is executed at the point of decoration of the function. Note that
we can call func() inside __init__(), showing that the creation of func() is complete before the decorator is called. Note
also that the decorator constructor receives the function object being decorated. Typically, one will capture the function
object in the constructor and use it later in the __call__() method.
When afunction() is called after it has been decorated, we get completely different behaviour; the adecorator.__call__()
method is used instead of the original code. That's because the act of decoration *replaces* the original function
object with the result of the decoration, i.e. the adecorator object replaces afunction.
Note that the constructor stores the argument, which is the function object.
'''

'''
Since a function object is also callable, functions can be used to properly replace the decorated function. The following
is equivalent to the above example which used a class as the decorator
'''

def entry_exit(func):
    def new_func():
        print "Do something before %s is properly called..." % func.__name__
        func()
        print "Do something before %s is properly exited..." % func.__name__
    return new_func

@entry_exit
def func1():
    print "inside func1()"

@entry_exit
def func2():
    pass

func1()
func2()

'''
In the above, new_func() is defined within the body of entry_exit(), so is created and returned when entry_exit() is
called. Note that new_func() is a CLOSURE, because it captures the actual value of func.
Once new_func() has been defined, it is returned from entry_exit(), so that the decorator mechanism can assign the result
as the decorated function.
The info you can get dynamically about functions, and the modifications you can make to those functions, are powerful!
'''

'''
In the class example above, the decorator does not have arguments and neither do the functions. If the functions did have
arguments, then when the function to be decorated is passed to the constructor, and
subsequently the __call__() method is called whenever the decorated function is invoked, any arguments for the decorated
function are passed to __call__(). Hence we must have __call__(self, *args). Args besides self are not required for
__init__() because __init__() is the method called to perform decoration
'''

'''
The decorator mechanism behaves quite differently when you pass arguments to the decorator. Let's modify the above
class decorator example to see what happens when we add arguments to the decorator:
'''

class another_decorator(object):

    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        print "Initialising with args...", self.arg1, self.arg2

    def __call__(self, func):
        print "inside __call__()"
        def wrapped_func(*args):
            print "Do something before %s is properly called..." % func.__name__
            func(*args)
            print "Do something before %s is properly exited..." % func.__name__
        return wrapped_func

@another_decorator("hello", "world")
def another_func(arg1, arg2):
    print "another_func is performing its function...", arg1, arg2

print "finished decorating"
another_func("goodbye", "my love")

'''
from the output, we can see how the behaviour has changed:
now the process of decoration calls the constructor *and then immediately invokes __call__()* (which in previous examples
was invoked only when the function was called after decoration). Here, __call__() can only take a single argument (the
function object) and must return the decorated functon object that replaces the original. Notice that __call__() is now
only invoked once, during decoration, and after that the decorated function that you return from __call__() is used for
the actual calls.
Although this behaviour makes sense - the constructor is now used to capture the decorator arguments, but the object
__call__() can no longer be used as the decorated function call, so you must instead use __call__() to perform the
decoration - it is nonetheless surprising the first time you see it because it's acting so much differently than the
no-argument case, and you must code the decorator very diffrently from the no-argument case
'''

'''
Now let's modify the function decorator to take arguments:
'''

def another_decorator_func(arg1, arg2):
    def wrap(func):
        print "inside wrap()"
        def wrapped_func(*args):
            print "inside wrapped_func()"
            print "decorator args:", arg1, arg2
            func(*args)
            print "after f(*args))"
        return wrapped_func
    return wrap

@another_decorator_func("hello", "world")
def yet_another_func(arg1, arg2):
    print "yet_another_func is performing its function...", arg1, arg2

print "finished decorating"
yet_another_func("goodbye", "my love")

'''
The return value of the decorator function must be a function used to wrap the function to be decorated. That is, Python
will take the returned function and call it at decoration time, passing the function to be decorated. That's why we
have three levels of functions; the inner one is the actual replacement function.
Because of closures, wrapped_func() has access to the decorator arguments arg1, arg2 and arg3, without having to
explicitly store them as in the class version.
'''

'''
We can use a pair of functions to wrap another function to be called. This is less elegant than the previous methods but
included for completeness. Let's see how to do this to use separate functions to perform operations before and after
a function is called:
'''

def wrap(pre, post):
    def decorate(func):
        def call(*args, **kwargs):
            pre(func, *args, **kwargs)
            result = func(*args, **kwargs)
            post(func, *args, **kwargs)
            return result
        return call
    return decorate

def trace_in(func, *args, **kwargs):
    print "Entering function %s ..." % func.__name__

def trace_out(func, *args, **kwargs):
    print "Leaving function %s ..." % func.__name__

@wrap(trace_in, trace_out)
def called_func(arg1, arg2, arg3=None, arg4=None):
    print arg3
    return arg1 + arg2

print called_func(1, 2, "quack", "honk")

'''
Two built-in decorators are @staticmethod and @classmethod. Let's have a look:
'''

class A(object):
    # function foo() without decorator
    def foo(self, x, y):
        self.x = x
        self.y = y
        print "executing foo() with args (%s,%s,%s)" % (self, x, y)

    @classmethod
    def class_foo(cls, x, y):
        print "executing class_foo() with args (%s,%s,%s)" % (cls, x, y)

    @staticmethod
    def static_foo(x, y):
        print "executing static_foo() with args (%s,%s)" % (x, y)

a = A()
a.foo("quack", "duck") # usual way for object instance to call a method. The object instance, a, is implicitly passed as the first argument
a.class_foo("honk", "goose")
A.class_foo("honk", "goose") # you can call class_foo() using the class (A) as well as the object instance (a) !
a.static_foo("hiss", "swan")
A.static_foo("hiss", "swan") # you can also call static_foo() using the class

'''
Notice the difference in the call signatures of foo, class_foo and static_foo
-with @classmethod, the class of the object instance is implicitly passed as the first argument instead of self
Normally something is defined to be a classmethod if you intend to call it from the class rather than the class instance
-with @staticmethod, neither self (the object instance) nor cls (the class) is implicitly passed as the first
argument. They behave like plain functions except that you can call them from an instance or from the class. Staticmethods
are used to group functions which have some logical connection with a class to the class, while indicating that it does
not require access to the class - i.e. a staticmethod is a method that knows nothing about the class or instance it
was called on, it just gets the arguments that were passed to itself.

When to use @classmethod and @staticmethod :
Let's think about an example

The class A is used to store information about waterfowl. Let's write a slightly different class that uses an __init__()
'''

class Waterfowl(object):

    def __init__(self, noise, bird):
        self.noise = noise
        self.bird = bird

    @classmethod
    def get_bird(cls, bird_as_integer):
        if bird_as_integer == 0:
            bird = "duck"
            noise = "quack"
        elif bird_as_integer == 1:
            bird = "goose"
            noise = "honk"
        elif bird_as_integer == 2:
            bird = "swan"
            noise = "hiss"
        abird = cls(noise, bird)
        return abird

    @staticmethod
    def validate_bird(bird_as_integer):
        return bird_as_integer < 3


'''
Let's assume that we want to create a lot of Waterfowl instance classes, but that bird species are are encoded as integers
in various places in the code. We want to get this information back into a string (the bird name) and then instantiate
Waterfowl by passing these values to initialisation call. @classmethod is ideal for this, acting as another constructor.
Fulfils the same purpose as overloading in C++. We've implemented parsing input to instantiate a class in one place and
its reusable. Note that because cls is an object that holds the class itself, and not an instance of the class, then if
we inherit our Waterfowl class, all children will have get_bird defined also
'''

a_waterfowl = Waterfowl.get_bird(1)
print a_waterfowl.noise, a_waterfowl.bird

'''
@staticmethod is similar to @classmethod but doesn't take any obligatory parameters like a classmethod or instance
method does. @staticmethod is useful when a task is logically bound to the Waterfowl class, but still doesn't require
instantiation of it. For example, if we want to validate that an integer-encoded bird is a waterfowl before we
instantiate a class for it, we can have a staticmethod validate_bird for that
'''

abird = 2
if Waterfowl.validate_bird(abird):
    a_waterfowl_2 = Waterfowl.get_bird(abird)
    print a_waterfowl_2.noise, a_waterfowl_2.bird

'''
As we can see, a @staticmethod doesn't have any access to what the class is; it's basically just a function, called
syntactically like a method, but without accesss to the object and its internals (fields and other methods) while a
@classmethod does
'''
