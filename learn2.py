is_active = True
is_admin = False
print(is_active)

a = bool('Hi')
print(a)

# price = input('Enter the price: ')
# tax = input('Enter the tax rate: ')

# tax_amount = int(price) * int(tax) /100

# print(f"The tax amount price is ${tax_amount}")


x = 1
z = float(x)
print(z)

for x in "banana":
    print(x)


text = "The best things in life are free!"
if "mom" not in text:
    print("No, 'free' is not present.")

print(text.lower())

age = 54
txt = "My name is John, and I am {}"
print(txt.format(age))

k = 200
l = 300

if k > l:
    print("k is greater")
else:
    print("l is greater")


myList = ["apple", "orange", "cherry","banana"]
# myList.remove("orange")
# myList.clear()

# for x in myList:
#  print(x)
# print(type(myList))

'''i = 0
while i < len(myList):
  print(myList[i])
  i = i + 1

newlist =  [x if x != "banana" else "orange" for x in myList]
print(newlist)

myList.sort()
print(myList)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)'''

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)