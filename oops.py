# OOPS

# CLASS
# # _init_
# # All classes have a function called __init__(), which is always executed when the class is being initiated.
# # Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# # The __str__() function controls what should be returned when the class object is represented as a string.
# # If the __str__() function is not set, the string representation of the object is returned:
# # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# # It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def __str__(self):
#     return f"{self.name}({self.age})"

#   def myfunc(self):
#     print("Hello my name is " + self.name)
# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)

# Python Inheritance

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()

# class Student(Person):
#   def __init__(self, fname, lname, year):
#     super().__init__(fname, lname)
#     self.graduationyear = year

#   def welcome(self):
#     print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# # Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# # Iterator
# # Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)

# POLYMORPHISM

# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class

# for x in (car1, boat1, plane1):
#   x.move()