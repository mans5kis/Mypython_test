# strings
word = "my age is didn't happen"
word2 = 'hi5!'
print(word)

word3 = "  hello, titan  "
print(word3[-5:-1])
print(len(word3))
print(word3.strip())

print(word.lower())
print(word.upper())

a = 'maanas'
print(a.replace('s', 'sur'))

print(a.split('a'))

print('helw' in word3)
print('hel' in word3)
# mansur please check all stings
a1 = 'hai'
a2 = 'mans'
print(a1 + " " + a2)  # this is concadenation

# Boolean means either true or false
print(1 > 10)
print(10 > 1)
print(10 == 10)
# logical operator  means and or not
# identity operator  is , is not
# membership operator in not , in
# bitwise operator & ~  <<

number1 = 10
number2 = number1 + 20
number1 += 10
print(number1)

# casting# ###
a = float(10)
b = 10.10
d = 'h3'
print(a, b)

# Type keyword
print(type(d))

# list
fruits = ['apple', 'orange', 'mango', 'apple']
fruits[1] = 'banana'
fruits.append("new")
print(fruits)
print(len(fruits))

number = [11, 2, 20, 10]
number.sort()
print(number)

numbers = [11, 2, 20, 10]
numbers.sort(reverse=True)
print(numbers)

add = fruits + number + numbers
print(add)

# tuples -  cannot modify the content
fruits2 = ('apple', 'water')
print(fruits2)

# set {} same as above

# Dictionary , get
my_data = {
    "name": "mans",
    "age": "33"
}
# my_data["age"] = "35"
print(my_data)
print(my_data.get("age"))

# if, else, else if condition statement
age = 30
if age > 20:
    print("you are rock")
else:
    print(" you are not rock")

a, b = 10, 20
if a == 10 and b == 20:
    print("correct")
else:
    print("incorrect")

# nested if (if inside if)
a, b = 10, 20
if a == 10 or b == 20:
    print("correct")
    if b == 20:
        print("true")
else:
    print("incorrect")


# functions def is the keywoard addition is the function#

def addition():
    m = 23
    n = 45
    print(m + n)
addition()


def addition(m, n):
    print(m + n)
addition(12, 10)
addition(100, 300)


def substraction(l,c):
    print(l - c)

substraction(10, 2)
substraction(100, 50)

def hi(name):
    print("Hi," + name)
hi("mans")

# Function written
def fun():
    return 100
print(fun())

def fun(a):
    return a * 100
print(fun(5))

# loops range (one time written multiple time runs)

# for loop
names  = 'mansur'
for letters in names:
     print(letters)

fruits3 = ['apple', 'banana', 'mango']
for mfruits in fruits3:
     print(mfruits)


for i in "hi, welcome":
    print(i)

for i in "hi, welcome mans":
    if i == ',':
        print(", is present")

for i in "hi, welcome mansr":
    if i == ',':
        print(", is present")
    else:
        print(", is not presents")

for i in "hi, mansur":
    if i == ',':
        print(", is present")
        break
    else:
        print(", is not present")

for i in "hi, welcome mans":
    if i == ',':
        continue
    else:
        print(", is not available")

# range 5- 0,1,2,3,4

for number33 in range(5):
    print(number33)
#
for number34 in range(2, 6):
    print(number34)

for number35 in range(10, 30, 4):
    print(number35)

for number23 in range(5):
    print(number23)
else:
    print("all numbers are finished")

# while  loop

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("over")

# lambda
add_5 = lambda number: number + 10
print(add_5(120))
print(add_5(34))


# inputs
#number6 = int(input('enter number 1'))
#number7  = int(input('enter number 2'))
#print(number6 + number7)

#name22 = input("please enter you name")
#print("my name is" + name22)

# simple  calculator

def add(a, b):
    return a+b

def sub(a, b):
    return a-b
def div(a, b):
    return a//b
def mul(a, b):
    return a*b

print("""select your operation
1.add
2.sub
3.div
4.mul
""")

choice = int(input("enter your choice"))
a = int(input("enter first numbers 1"))
b = int(input("enter second numbers 2"))
if choice == 1:
    print(add(a, b))
elif choice == 2:
    print(sub(a, b))
elif choice == 3:
    print(div(a, b))
elif choice == 4:
    print(mul(a,b))
else:
    print("enter correct choice")


# Task
