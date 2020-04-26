'''
Illustration of the property decorator in Python

the property object acts as a descriptor, which means it has its own __get__(), __set__() and
__delete__() methods. The __get__() and __set__() methods are triggered on an object when a
property is retrieved or set, and __delete__() is triggered when a property is deleted with del.
'''

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = None # double leading underscore: "name mangling". Private attribute

    @property
    def age(self):
        print "    > Called age getter"
        return self.__age

    @age.setter
    def age(self, age_val):
        print "    > Called age setter"
        self.__age = age_val

    @property
    def full_name(self):
        print "    > Called full name getter"
        return self.first_name + " " + self.last_name

    # wrap the full_name "set()" function so that it acts to update first_name and last_name
    @full_name.setter
    def full_name(self, value):
        print "    > Called full_name setter"
        first_name, last_name = value.split(" ")
        self.first_name = first_name
        self.last_name = last_name

    @full_name.deleter
    def full_name(self):
        print "    > Called full_name deleter"
        del self.first_name
        del self.last_name


person = Person("Billy", "Bob")
print "first name: %10s  second name: %10s" % (person.first_name, person.last_name)
person.age = 35
print "age: %i" % person.age
print "full name: %s" % person.full_name
# trigger the __set__() method for full_name, which was inherited from "object" (hence class *must*
# inherit from "object")
print "now change name..."
person.full_name = "Timmy Tom"
print "full name: %s" % person.full_name
del person.full_name
try:
    print "first name: %s" % person.first_name
except AttributeError:
    print "AttributeError thrown: person's first name has been deleted!"
