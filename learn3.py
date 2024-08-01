import mymodule
import platform
import datetime
import json
import re
print('opoku') 

myTuple = ("apple", "banana", "cherry", "apple")
print(myTuple)
print(len(myTuple))
print(myTuple[3])

if "cherry" in myTuple:
    print('found cherry')


x = ("apple", "banana", "cherry")
t = x.index("cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
print(t)
#set

mySet = {"apple", "banana" , "cherry"}
mySet.add("orange")
r = mySet.pop()
print(mySet)
print(r)

#dictionary

myDic = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(myDic)
print(myDic["brand"])
print(len(myDic))


k = 33
u = 300
m = 78
if u > k:
    print("u is greater than k")
elif k > u:
    print("k is greater than u")

if k < u and m > k: print("k is less than u")

i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


frutelli = ["mango", "orange", "cherry"]
for x in frutelli:
    print(x)


for x in range(2, 6):
  print(x)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


def my_function():
   print("hello from my function")

my_function()

def our_func(fname):
   print(fname + " " + "rehearse more")


our_func("email")

def func(x):
   return 5 * x

print(func(4))


x = lambda a : a + 10
print(x(5))

y = lambda a, b : a * b
print(y(5,6))

def myfunc(n):
   return lambda a : a * n
mydoubler = myfunc(2)

print(mydoubler(11))

mymodule.greeting("jonathan")
x = platform.system()
z = dir(platform)
print(x)
print(z)
w = datetime.datetime.now()
print(w)

p = min(5, 39, 35)
print(p)

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)

print(json.dumps(True))
print(json.dumps(31.76))


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)