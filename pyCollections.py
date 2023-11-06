# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# List
# thislist = ["apple", "banana", "cherry"]
# print(thislist)

# List() constructor

# Access Items
# thislist[1]

# change list items
# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"
# print(thislist)

# thislist.append("orange")
# thislist.insert(1, "orange")

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)

# can extend any iterable be it set,tuple,dict

# thislist.remove("banana")
# thislist.pop(1)
# del thislist[0]
# del thislist
# thislist.clear()

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]

# thislist.sort()
# thislist.sort(reverse = True)
# thislist.sort(key = str.lower)
# thislist.reverse()

# mylist = thislist.copy()

# list methods
# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# Tuples

# thistuple = ("apple", "banana", "cherry")

# thistuple = tuple(("apple", "banana", "cherry"))

# indexing

# y.append("orange")
# y.remove("apple")
# del thistuple

# fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

# (green, *tropic, red) = fruits

# tuple methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# SETS

# no duplicates

# set1 = {"abc", 34, True, 40, "male"}

# thisset = set(("apple", "banana", "cherry"))

# Access Items
# You cannot access items in a set by referring to an index or a key.

# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)

# thisset.add("orange")

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# thisset.remove("banana")
# thisset.discard("banana") discard doesnt raise error if item doesnt exits
# x = thisset.pop()
# thisset.clear()
# del thisset

# set3 = set1.union(set2)

# set1.update(set2)

# x.intersection_update(y) Return a set that contains the items that exist in both set x, and set y:


# x.symmetric_difference_update(y) Keep the items that are not present in both sets:

# Set Methods

# Method	Description
# add()	Adds an element to the set
# clear()	Removes all the elements from the set
# copy()	Returns a copy of the set
# difference()	Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	Remove the specified item
# intersection()	Returns a set, that is the intersection of two other sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	Returns whether two sets have a intersection or not
# issubset()	Returns whether another set contains this set or not
# issuperset()	Returns whether this set contains another set or not
# pop()	Removes an element from the set
# remove()	Removes the specified element
# symmetric_difference()	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	Return a set containing the union of sets
# update()	Update the set with the union of this set and others

# Python Dictionaries

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# value of any datatype

# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# thisdict = dict(name = "John", age = 36, country = "Norway")

# Accesing
# x = thisdict.get("model")
# x = thisdict.keys()
# x = thisdict.values()
# x = thisdict.items()

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.keys()

# print(x) #before the change

# car["color"] = "white"

# print(x) 

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"year": 2020})

# thisdict.pop("model")

# thisdict.popitem() last inserted item

# del thisdict["model"]
# thisdict.clear()

# for x, y in thisdict.items():
#   print(x, y)

# mydict = thisdict.copy()

# mydict = dict(thisdict)

# print(myfamily["child2"]["name"])

# Dictionary methods
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary