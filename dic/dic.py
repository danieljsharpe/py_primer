import collections

'''A dictionary is a flexible object for storing various kinds of information, esp. when reading files. Roughly speaking,
a list where the index can be a text (as opposed to an integer) is a Python dictionary.
e.g. consider storing the temperatures of different cities in a dictionary:'''

temps = {'Oslo': 13.0, 'London': 15.4, 'Paris': 17.5}
#or, equivalently...
temps = dict(Oslo=13.0, London=15.4, Paris=17.5)
#add another text-value pair
temps['Madrid'] = 26.0
#print info in dict
for city in temps:
    print "Temp. in %s is %g" % (city, temps[city])

'''The string "indices" in a dictionary are called KEYS, and the 'elements of the dictionary are VALUES. Key/value pairs
are referred to as ITEMS'''
# "key in dic" statement returns Boolean expression
print 'Oslo' in temps
# keys, values and items can be extracted as lists from a dictionary (the latter is a nested list)
print temps.keys()
print temps.values()
print temps.items()
# a key-value pair can be removed from the dictionary
del temps['Oslo']
print len(temps)

'''We can take a copy of a dictionary. This avoids the fact that if two variables refer to the same dictionary, then changing the
contents of the dict through either of the variables will affect both variables'''
temps_copy = temps.copy()
del temps_copy['Paris']
print temps, temps_copy

'''The keys in a dictionary can be any IMMUTABLE object (i.e. any object whose contents cannot be changed). Such data types in
Python are int,float,complex,str & tuple'''
#consider a stock of exotic GM fruit, use tuples as keys
fruitstock = {("banana","blue"): 24, ("apple","purple"): 12, ("banana","pink"): 5, ("mango","pink"): 14}
for key in fruitstock:
    print "Fruit:", key[0], "Colour:", key[1], "No. in stock:", fruitstock[key]
#for this purpose we could also consider namedtuple() in conjunction with dict
#namedtuple() is a factory function for creating tuple subclasses with named fields
Fruit = collections.namedtuple("Fruit", ["name","color"])
f = Fruit(name="banana",color="red")
print f.name, f.color
fruitstock[(f.name,f.color)] = 5
print fruitstock
print fruitstock[f]
#sort according to key (here, key[0] (and then key[1] if same key[0]) since key is a tuple) alphabetically
fruits = fruitstock.keys()
fruits.sort()
print fruits

#let's make a new dictionary from our namedtuple
f2 = Fruit(name="banana",color="blue")
f3 = Fruit(name="strawberry",color="green")
fruitstock2 = {f: 5, f2: 7, f3: 2}
print fruitstock2
fruits2 = fruitstock2.keys()
#sort according to key[1] alphabetically
fruits2.sort(key=lambda x:x.color)
print fruits2
#get a list of all colors of one fruit
bananas = [fruit.color for fruit in fruits2 if fruit.name=="banana"]
print bananas

'''The order of the returned list of keys is unpredictable. If the keys need to be traversed in a certain order, you can sort
the keys, for example a loop over the keys in the temps dictionary in alphabetical order is achieved using the built-in
sorted() function:'''
for city in sorted(temps):
    print city

'''OrderedDict is a dict subclass (in the module collections) that remembers the order of key-value pairs as they
were created:'''
temps_ord = collections.OrderedDict(Copenhagen=12.3,Warsaw=15.0,Prague=16.1)
print temps_ord
