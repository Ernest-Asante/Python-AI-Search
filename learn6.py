#tuple = (ordered, unchangeable, use to group related data)

"""student = ("bro", 21, "male")

print(student.count("bro"))
print(student.index("male"))


for x in student:
    print(x)

if "bro" in student:
    print("welcome bro")"""


#set = (unordered, unindexed, no duplicate)

'''utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")

print(utensils)

for x in utensils:
    print(x)'''

#dictionary = (changeable, unoreded, key:value pair)

"""capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            'China': "Beijing",
            "Russia": "Moscow"
        }
 
capitals.update({"Germany":"Berlin"})
print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())"""

#function

def repeat():
    print("hello function")

repeat()

def hello(name):
    print("hello " +name)

hello("kwame")

def multiply(num1, num2):
    result = num1 * num2
    return result

x = multiply(5,6)

print(x)

#nested function
#variable scope

def display_name():
    name = "Code"
    print(name)

#args
    
def add(*args):
    sum = 0
    for i in args:
        sum +=i
    return sum

print(add(1,2,6))

#kwargs

"""def hello(**kwargs):
    print("Hello", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

hello(first = "Bro", middle = "Dude", last = "Code")"""

# str.format()

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)