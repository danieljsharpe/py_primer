''' Python script illustrating how names and references work for mutable objects in Python '''

class Foo(object):

    def __init__(self):
        self.list_var = [7,8,9]
        self.int_var = 100

    def changevars(self):
        # lists are mutable, so here we are pointing a new name at the same instance
        list_var = self.list_var
        # changes to list_var therefore affect the underlying object (namely, self.list_var)
        list_var[0] = 6
        list_var.pop()
        # list_var = [10,11,12] # this re-assigns the name list_var: it does not change self.list_var because list_var becomes
                                # no longer a name for self.list_var !
        # here we make a *copy* of self.list_var
        list_var_copy = self.list_var[:]
        # any changes to list_var_copy have no effect on self.list_var
        list_var_copy[0] = 5
        list_var_copy.pop()
        # int_var takes the value of self.int_var. int objects are immutable - we cannot change self.int_var via int_var
        int_var = self.int_var
        # this statement re-assigns int_var, int_var is no longer a name for self.int_var
        int_var = 200

# note we could make a subclass of int and add methods so that objects of the subclass are mutable
# or we could create a class that stores an int (and has an __index__ method to define how to and objects of which are mutable
class IntLike(object): # not IntLike(int):
    def __init__(self, value=0):
        self.value = value
    def __index__(self):
        return self.value

myfoo = Foo()
myfoo.changevars()
print myfoo.list_var
print myfoo.int_var
