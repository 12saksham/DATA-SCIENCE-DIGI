print('Hello World')
print(5)
print(77)
print("hay i am good boy\nviwers is also good")


# Type Casting
a = 1.09987876765668878
print(a)
c = 23
b = 67
print(c + b) 

a = "5"
b = "6"
print(a + b )
print(int(a) + int(b) )

a = int("5")
b = int("6")
print(a + b )

# Two types of Casting
# 1 Explit Conversion
# 2 Implict Conversion

# EX Implict Conversion

e = 4.8
type(e)
f = 2
type(f)
z = e + f
print(z)
type(z)

# Taking User Input in Python

# a = input("Enter Your Name: ")
# print('My Name is', a)

# x = input("Enter your 1 number: ")
# y = input("Enter your 2 number:" )
# print(int(x)+ int(y))

#String in python
name = "saksham"
friend = "shreyansh"
anotherFriend = "Abhinav"
apple = "he said, \"I want to eat an apple"
print("hello", name)
print(apple)

name = "saksham"
friend = "shreyansh"
anotherFriend = "Abhinav"
apple = 'he said, "I want to eat an apple'
print("hello", name)
print(apple)

name = "saksham"
friend = "shreyansh"
anotherFriend = "Abhinav"
apple = 'he said, "I want to eat an apple'
print("hello", name)
print(apple)
print(name[0] )
print(name[1] )
print(name[2] )
print(name[3] )
print(name[4] )
print(name[5] )
print(name[6] )
#print(name[7] )# index error mean in nothing in object

name = "saksham"
friend = "shreyansh"
anotherFriend = "Abhinav"
apple = '''he said, 
Hi Saksham
hey i am good
"I want to eat an apple'''
print("hello", name)
print(apple)
print("Let use for loop")
for charater in name:
    print(charater)
for charater in apple:
    print(charater)

# String Slicing
name = 'saksham,sumit'
# print(len(name))
# print(name[0:7])
# print(name[:7])
# print(name[2:9])
# print(name[0:-7])
print(name[-9:-6]) #[4:7] (len of name - 9, len of name - 6) (13-9, 13-6)

#Quick quiz
nm = "Harry"
print(nm[-4:-2])










