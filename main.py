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