print("Hey , this is Ariyan!")
#Hello i am Ariyan. Thisis single line comment.
"""doctsring for multi line comments"""
#variables
Ariyan = 51

#camel case 
ariyanMahammad=51
#pascal case 
AriyanMahammad=51
#snake case 
Ariyan_Mahammad=51

#data types 
a=10 #Integer
b=10.5 #float
c=10/2 #float--any number or fraction having pq term is float

d=10j #complex
#Strings - '' or ""
Name = "Sk Ariyan Mahammad" # string data type

Success = True # boolean data type

"""
1. ord()

ord() returns the Unicode (ASCII for common English characters) value of a character.
Syntax: 
ord(character)
Examples: 
print(ord('A'))

Output:

65

2. chr()

chr() does the opposite.

It converts a Unicode number into its corresponding character.

Syntax:
chr(number)
Examples:
print(chr(65))

Output:

A
"""
print(ord('A'))
print(chr(65))
print("Ariyan")
for i in range(ord('A'), ord('Z') + 1):
    print(chr(i), end=" ")

#indexing 1. positive 2. negative 

#string slicing
a= "Sher Coder"
#a[start:stop:steps]
print("\n",a[5:10:1])

#type conversion

#input 
# a=input("Enter a number : ")
# print("the number is : ",a)

# name = input("Enter your name : ")
# print(f"Your name is {name}") #f sring format
"""default data type of input is string , so we have to use int(input()) , when we will work with numerical data type"""

#operators

a=10
b=5

print(a/b) #2.0
print(a//b) #2 , this is floor division
print(2**3) #8 - ** is power

#BODMAS - brackets , orders , division , multiplication , subtraction
#if-else if-elif-else
box = ""
if box==10:
    print("Give lays!")  #five spaces or tab
else: 
    print("No lays!")


# gender = input("Enter your Gender : ").lower()
# if gender == "male":
#     print("hello sir , how can i help you!")
# elif gender =="female":
#     print("hello ma'am , how can i help you!")

# else :
#     print("Invalid gender!")

#loops
#range(start , stop , steps)

for i in range(1,11):
    print(i)


def sum(x,y):
    return x+y

print(sum(2,4))


def palindrome(string):
    if string == string[::-1]:
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

# palindrome(input("Enter a string : "))

#data structures in python 

#list
#tuple
#dictionary
#set

#list - mutable
#tuple - immutable
#dictionary - mutable
#set - mutable

# list - []
# tuple - ()
# dictionary - {}
# set - {}

#example -list
list1 = [1,2,3,4,5]
print(list1)
print(list1[0])
print(list1[-1])
print(list1[1:4])
list1.append(6)
print(list1)
list1[3] = 10
print(list1)

#example -tuple
tuple1 = (1,2,3,4,5)
print(tuple1)
print(tuple1[0])
print(tuple1[-1])
print(tuple1[1:4])

#example -dictionary
dict1 = {1:"A",2:"B",3:"C",4:"D",5:"E"}
print(dict1)
print(dict1[1])
print(dict1.keys())
print(dict1.values())
print(dict1.items())

#example -set
set1 = {1,2,3,4,5}
print(set1)
set1.add(6)
print(set1)
set1.remove(6)
print(set1)

#when to use which data structures 

