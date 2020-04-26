#Use of 'magic variables' *args & **kwargs in Python

#*args and **kwargs allow you to pass a variable number of arguments to a function, in case you do not know beforehand
#how many arguments can be passed to your function

#*args is used to send a NON-KEYWORDED variable length argument list to the function. Example:
def test_var_args(f_arg, *args):
    print "first, normal arg:", f_arg
    for arg in args:
        print "another arg through *args:", arg

test_var_args('yoghurt','ham','spam','eggs')

#**kwargs allows you to pass KEYWORDED variable length (dictionary) of arguments to a function. **kwargs should be used if you want
#to handle NAMED ARGUMENTS in a function. Example:
def test_var_kwargs(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "key:", key, "\tvalue:", value

test_var_kwargs(food_1='yoghurt', food_2='ice cream')
food_dict = {'yoghurt': 'raspberry', 'ice cream': 'strawberry', 'ice cream': 'banana'}
try: test_var_kwargs(food_dict)
except TypeError: print "Passing a dictionary as **kwargs doesn't work" # Because what happens is that **kwargs is converted to a dict!
#Using **kwargs provides us with flexibility to use keyword arguments in our program

#ORDERING ARGUMENTS:
'''
#PYTHON 3: when ordering arguments within a function or function call, arguments need to occur in a particular
#order: 1. formal (explicit) positional args (params) 2. *args 3. (named) keyword args (params) 4. **kwargs
def fishes(arg_1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):
    print "I have %i fish in one tank and %i fish in another" % (arg_1, arg_2)
    for arg in args:
        print "My fish eat", arg
    print "My favourite fish are %s and %s" % (kw_1, kw_2)
    if kwargs is not None:
        print "I also want a new shark:"
        for key, value in kwargs.iteritems():
            print key, value
#Note that if you want to pass kwargs, you will have to pass the named keyword args kw_1 & kw_2 (even though they are 'optional').
#Similarly if you want to pass *args, you have to specify the keyword args kw_1 and kw_2

fishes(2, 2, 'spam', 'ham' 'eggs', 'shark', 'blowfish', species='hammerhead', size='large')
'''
'''
#ALSO IN PYTHON 3: there is the ability to use a lone "*" as a placeholder if there are no *args but there are keyword args and **kwargs
e.g.
def fishes(arg_1, arg_2, *, kw_1="shark", kw_2="blobfish", **kwargs)
    return
'''
#PYTHON 2: order is: func(arg_1, arg_2, kw_1, kw_2, *args, **kwargs)
def fishes(arg_1, arg_2, kw_1="shark", kw_2="blobfish", *args, **kwargs):
    print "I have %i fish in one tank and %i fish in another" % (arg_1, arg_2)
    for arg in args:
        print "My fish eat", arg
    print "My favourite fish are %s and %s" % (kw_1, kw_2)
    if kwargs is not None:
        print "I also want a new shark:"
        for key, value in kwargs.iteritems():
            print key, value
#Note that if you want to pass args or kwargs, you will have to pass the named keyword args kw_1 & kw_2 (even though they are 'optional')
#This is the only possible ambiguity; *args and **kwargs cannot be confused because only the latter are named / keyworded

fishes(2, 2, 'shark', 'blowfish', 'spam', 'ham', 'eggs', species='hammerhead', size="large")
