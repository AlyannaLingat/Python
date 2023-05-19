"""
#basic programming
print("what is your name?")
name = input("Name: ")
print("Hello, " + name)

#if else
print("Input a number")
n = int(input("Number: "))

if n > 0:
    print ("n is positive")
elif n < 0:
    print ("n is negative")
else:
    print ("n is zero")
"""
"""
#sequences
name = "Seimon"
print(name[1])
"""
"""
#Define LIST of names
names = ["Harry", "Ron", "Hermione","Ginny","Valdemort"]
names.append("Draco")
names.sort()
print (names)

#Create empty SET
s =set()
#Add value on SET
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
print(s)
print(f"The set has {len(s)} elements")
"""
"""
#LOOPS
for A in [0,1,2,3,4,5,6,7,8,9,10]:
    print(A)
#with Range
for a in range (11):
    print(a)
#Loop for list names
names = ["Harry", "Ron", "Hermione","Ginny","Valdemort"]
for name in names:
    print (name)
#Loop for list characters
name = "Harry"
for character in name:
    print(character)
"""
"""
#Dictionaries
houses = {"Harry": "Griffindor", "Ronald": "Griffindor", "Hermione": "Griffindor", "Draco": "Slytherin"}
print(houses["Harry"])
"""
"""
#Functions 
#def meaning define 
def square (x): 
    return x*x
for a in range(11):
    print(f"The value of {a} is {square(a)}")
#Squares
#from fuctions import square = meaning tinatawag ng square yung fucntion sa kabilang file.
for a in range(11):
    print(f"The value of {a} is {square(a)}")
"""
"""
#Classes
#underscore  underscore init underscore is a method or fuction is going to authomatically be called 
#every time that I try to create a new point
class Point():
    def __init__(self, input1, input2):
        self.x=input1
        self.y=input2
p=Point(10,18)
print(p.x)
print(p.y)
"""
"""
#classes Flight

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def Add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)    
flight = Flight (5)       
    
people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    success = flight.Add_passenger(person)
    if success:
        print(f"Added {person} to flight successfuly.")
    else:
        print(f"No available seats for {person}")
"""
"""
#Decorators
def announce(f):
    def wrapper():
        print("About to run the function.....")
        f()
        print("Done with the fuction.")
    return wrapper

@announce
def hello():
    print("HELLO WORLD!!!")

hello()
"""
"""
#Lambda
people = [
    {"name": "Harry", "House": "Gryffindor"},
    {"name": "Cho", "House": "Ravenclaw"},
    {"name": "Cho", "House": "Syltherin"}
]

def f(person):
    return person ["name"]
#people.sort(key=lambda person: person["name"])
people.sort(key=f)
print(people)
"""
"""
#exception
#from unittest import result
import sys 
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid Input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot Divide by 0.")
    sys.exit(1)

print(f"{x}/{y} = {result}")
"""
"""
#bot
print("BOT: What is youre name?") 
Name = input("> ")
print("Hello, Ms/Mr:" + Name)
print("BOT: How are you ? ")
a = input("> ")
print("BOT: Good to know that, Ms/Mr: " + Name)
print("BOT: How may I help you? ")
a = input("> ")
print("BOT: List the Name of the passengers ")
a = input("> ")
print("BOT: This is your Flight ")

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def Add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)    
flight = Flight (5)       
    
people = ["Harry", "Ron", "Hermione", "Ginny", "Draco", "Snape", "Dumbledor"]
for person in people:
    success = flight.Add_passenger(person)
    if success:
        print(f"Added {person} to flight successfuly.")
    else:
        print(f" Sorry No available seats for {person}")
print("BOT: Thank you and have a nice day!")
"""

