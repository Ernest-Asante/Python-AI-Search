num1 = 51
num2 = 16

sum = num1 + num2
#print(sum)

if 5>2:
  print("Five is greater than two")

def main():
  i = 1
  max = 10
  while(i < max):
    print(i)
    i = i +1

main()

s = 'this is a string literal'
print(s)

help_message = '''
Usage: mysql command
-h hostname
-d database name
-u username
'''
print(help_message)

name = 'John'
message = 'Hi'
print(message)

greeting = name + message + '!'
print(greeting)

str = "Python String"
print(str[2])
print(str[-2])

str_len = len(str)
print(str_len)
print(str[0:3])

new_str = 'J' + str[1:]
print(new_str)
