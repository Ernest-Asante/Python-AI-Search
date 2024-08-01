class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + " I am " + str(self.age) + " years old")

p1 = Person("John", 36)
p1.myfunc()

name  = "Bro"
print("Hello" +" "+name)
#print(len(name))
#print(name.find("o"))
#print(name.upper())
#print(name.isalpha())
#print(name.count('r'))
#print(name.replace('r', 'h'))

#x = 1
#y = 2.0
#z = "3"

#x = float(x)
#y = int(y)
#z = int(z)

#print(x)
#print(y)
#print(z*3)

#firstName = input("what is your firstname?: ")
#print('Hello ' + firstName)

#import math

#pi = 3.14
#x = 1
#y = 2
#z = 3

#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
#print(max(x,y,z))

#myname = "opokukwame"
#website = "https://google.com"

#first_name = myname[0:5]
#print(first_name)

#slice = slice(8,-4)
#print(website[slice])

#age = -3

"""if age >= 24:
  print("you are older")
elif age < 0:
  print("you have not been born yet")
else:
  print("you are a child")

ages = ""
if not (ages):
  print("not")"""

#for i in range(10):
#  print(i)

"""rows = int(input("how many rows?: "))
columns = int(input("how many columns?: "))
symbol = input("enter symbol to use?: ")

for i in range(rows):
  for J in range(columns):
    print(symbol, end="")
  print()"""

"""while True:
  name = input("enter your name: ")
  if name != "":
    break"""


"""food = ["pizza", "hambugger", "hotdog", "spaghetti"]
print(food)

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0,"cake")

for x in food:
  print(x) """

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food[0][1])