# n = int(input("Number: "))
# if n > 0:
#     print("n is positive")
# elif n < 0:
#     print("n is negative")
# else:
#     print("n is 0")
# ---------------------------------

# name = ["Harry", "Ron", "Hermione"]
# print(name[1])
# -----------------------------------
#Tupples
# coordinate = (10.2, 5.3)
# print(coordinate)
# -----------------------------------
#Sorting
# names = ["Harry", "Ron", "Hermione"]

# names.append("Draco")

# names.sort()

# print(names)
# -----------------------------------
#Set
# s = set()
# s.add(1)
# s.add(2)
# s.add(3)
# s.add(4)
# print(f"Number of items in the set is {len(s)}")
# ------------------------------------
#Loops
# names = ["Harry", "Ron"]
# for i in names:
#     print(i)
# ------------------------------------
#Dictionary
# houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}

# houses["Hermiony"] = "Gryffindor"

# print(houses["Harry"])
# ------------------------------------
#Functions
# def square(x):
#     return x * x

# for i in range(10):
#     print(f"The square of {i} is {square(i)}")
# ------------------------------------
#Points
# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# p = Point(8, 2)
# print(p.x)
# print(p.y)

# class Flight():
#     # Method to create new flight with given capacity
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.passengers = []

#     # Method to add a passenger to the flight:
#     def add_passenger(self, name):
#         if not self.open_seats():
#             return False
#         self.passengers.append(name)
#         return True

#      # Method to return number of open seats
#     def open_seats(self):
#         return self.capacity - len(self.passengers)

# flight = Flight(3)

# people = ["Harry", "Ron", "Hermione", "Ginny"]
# for person in people:
#     if flight.add_passenger(person):
#         print(f"Added {person} to flight.")
#     else:
#         print(f"No available seats for {person}")
# ------------------------------------
#Decorators
# def announce(f):
#     def wrapper():
#         print("About to run the function...")
#         f()
#         print("End of the function")
#     return wrapper

# @announce
# def hello():
#     print("Hello world.")

# hello()
# ------------------------------------
#Lambda
# from os import name


# people = [
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Cho", "house": "Ravenclaw"},
#     {"name": "Draco", "house": "Slytherin"}
# ]

# people.sort(key=lambda person: person["name"])
# print(people)
# ------------------------------------
#Exceptions
import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Provide number.")
    sys.exit(1)

try: 
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    sys.exit(1)

print(f"{x} / {y} = {result}")
print("Buy")