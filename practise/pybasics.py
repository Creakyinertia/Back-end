# indentation
# if 5 > 2:
#   print("Five is greater than two!")

# comments
# # or '''  '''

# casting
# x = str(3)    # x will be '3'
# y = int(3)    # y will be 3
# z = float(3)  # z will be 3.0

# illegal var names
# 2myvar = "John"
# my-var = "John"
# my var = "John"

# destructuring
# x, y, z = "Orange", "Banana", "Cherry"
# One Value to Multiple Variables
# x = y = z = "Orange"
# Unpack a Collection
# fruits = ["apple", "banana", "cherry"]
# x, y, z = fruits

# global keyword
# x = "awesome"
# def myfunc():
#   global x
#   x = "fantastic"
# myfunc()
# print("Python is " + x)

# Datatypes
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Random
# import random
# print(random.randrange(1, 10))

# checking
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

# Slicing
# b = "Hello, World!"
# print(b[2:5])

# string modifications
# a = "Hello, World!"
# print(a.upper())
# print(a.lower())
# print(a.strip())
# print(a.replace("H", "J"))
# print(a.split(","))

# concat
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)

# string format
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))

# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {2} pieces of item {0} for {1} dollars."
# print(myorder.format(quantity, itemno, price))

# Escape characters
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# BOOLEAN
# everything is truthy except
# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})

# operators
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Python Identity Operators
# is ex: x is y
# is not ex: x is not y

# Python Membership Operators
# in ex: x in y
# not in not ex: x not in y

# shorthand if
# if a > b: print("a is greater than b")
# shorthand if else
# print("A") if a > b else print("B")

# print("A") if a > b else print("=") if a == b else print("B")

# pass
# no arguments

# while loops
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")
  
# for loops
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)  
  
# for x in range(2, 30, 3): #3rd param is increment of sequence
#   print(x)

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")
  
# functions
# *args
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# **kwargs
# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

# to work with arrays in Python you will have to import a library, like the NumPy library.

# Array methods
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# lambda function
# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))

# Use lambda functions when an anonymous function is required for a short period of time.

