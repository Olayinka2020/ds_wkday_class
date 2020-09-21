from math import *

# a console is a place where python would output information. which is where the print statement sends our files to.

'''
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
'''

# a variable is like a container that stores for storing data-values.. 
# which makes it alot easy for us to manage and work with all different types of data inside our program

# data types => Strings, numbers and boolean

# name = "Rooney"
# job_description = "Data analyst"
# is_male = False

# print("Hello Guys")
# # print("My name is", name)
# print("My name is" + name)
# print("and I am a", job_description)
# print("yes", job_description)
# print("don't be like " + name)
# print(is_male)

# Strings
# print("Techstudio \nAcademy")

# Concatenation=> The process of taking a string and appending another string onto it

# boot_camp = "Techstudio Academy"
# print(boot_camp + " offers a fullstack web dev program")

# String functions
# a function is basically a block of code that we can run and it'll perform a specific operation for us.
# we can use functions to modify our strings and also get information about our strings.

# Return a copy of the string converted to lowercase.
# print(boot_camp.lower())
# print(boot_camp.upper())

# Return True if the string is an uppercase string, False otherwise.
# A string is uppercase if all cased characters in the string are uppercase andthere is at least one cased character in the string.

# boot_camp2 = boot_camp.upper()
# print(boot_camp2.isupper())

# print(boot_camp.upper().isupper())

# Return the number of items in a container.
# print(len(boot_camp))

# you can also get index of characters.
# print(boot_camp[0])

# the index fn will tell us where a specific character is located inside of our string.
# print(boot_camp.index("d"))

# Return a copy with all occurences of substring old replaced by new.
# print(boot_camp.replace("Techstudio", "Lambda"))

# Working with numbers in python
# Any python you write would most likely be dealing with numbers at some point.

# print(3 + 4)

# print(4 * (5-2) + (2/50))

        # modulus
# print(10 % 8)

# my_num = -69

# print(str(my_num) + " is my favorite number")

# print(floor(3.94))

# print(ceil(3.94))

# print(max(4,5))

# print(sqrt(16))


# name = input("Enter your name? ")
# age = input("How old are you? ")

# print("Hello, your name is", name, "and you are", age, "years old")

# Basic calculator
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")

# result = int(num1) + int(num2)

# print(result)

# color = input("Enter a color; ")
# plural_noun = input("Enter a plural noun; ")
# person = input("Insert that guy/babe name; ")

# print("Roses are " + color)
# print(plural_noun + " are blue")
# print("No go dey reason " + person + " wey no dey reason you")

                                # Practise

# weight_kg=55
# print("weight in pounds", int(2.2 * weight_kg))

# weight_lb = 2.2 * weight_kg
# # print(weight_lb)

# print("weight_kg initial value is: ", weight_kg)
# weight_kg =10000
# print("After updating, weight_kg final value is: ", weight_kg)
# print("The final value of weight_lb is: ", weight_lb)

# weight_lb = 2.2 * weight_kg
# print("The new value of weight_lb is: ", weight_lb)

                        
                         # Datatypes

# print("Hello " * 3)

# x= "datatype"
# print(type("datatype"))

# multiline = '''
# This string
# spans multiple 
# lines
# !!!
# '''

# print(multiline)
# print(type(multiline))

# print(type(5))
# print(type(-1000))
# print(type(6 - 33))

# print(type(10 / 3))
# print(type(1.3))
# print(type(22.))

# print(type(True))
# print(type(False))
# print(type(None))

# 4 / 1.3 == 4

# print(str(1) + '1')
# print(int('6') - 7)
# print(int(7.23))
# print(bool('5'))
# print(floor(4 / 1.3))


                        # Lists
# a list is a structure that we can use inside our python program to
# store lists of information/data. you can take a bunch of related data values
# and organize them inside of a list and we can use it throughout our
# program. this makes keeping track of our data a lot easier

# we create lists like we create variables in py. although with lists, the
# list name has to be as descriptive as it could be.

# whenever you write this => [], py knows you want to create a list

# marvel_avengers = ['Black Panther', 'Captain America', 'Thor', 'Iron Man']
# print(marvel_avengers)
# print(marvel_avengers[-2])
# marvel_avengers[2] = 'Dr. Strange'
# print(marvel_avengers)

# PRACTISE
# example = ['1', '2', '3', '4', '5']
# print(example)

# example = [1, True, None, ['word', 123], 'test'] + ['1', '2', '3', '4', '5']
# print(example)
# print(example[0])
# print(example[1])
# print(example[2])

# print(example[:2])
# print(example[0:2])
# print(example[:-2])
# print(example[3][1])

# print(example1 + example)

# List1 = [1, 2, 3, 4]
# List2 = List1
# List2 += [5, 6, 7]
# print("List 2 is: ", List2)
# print("List 1 is: ",  List1)

# print(id(List1))
# print(id(List2))

# .copy() is a method. Methods are special functions associated with an object and define what it can do. 

# list1 = [1, 2, 3, 4]
# list2 = list1.copy()
# list2 += [5, 6, 7]
# print("List 2 is: ", list2)
# print("List 1 is: ", list1)

# Other frequently used methods of lists include .append(): this adds a one-element list

# list1.append(77)
# print(list1)

# And .extend() (combines two lists, instead of adding the second list as an element):

# list1.extend([99, 88, 101])
# print(list1)

# And of course, .remove() and .clear() (both do exactly what you think they should do):

# list1.remove(88)
# print(list1)

# list1.clear()
# print(list1)

# And .extend() (combines two lists, instead of adding the second list as an element):

# marvel_avengers = ['Black Panther', 'Captain America', 'Thor', 'Iron Man']
# list1 = [3, 4, 5, 6, 8]

# marvel_avengers.append("Dr Strange")
# print(marvel_avengers)

# marvel_avengers.extend(list1)
# print(marvel_avengers)

# marvel_avengers.insert(2, "Spiderman")
# print(marvel_avengers)

# marvel_avengers.remove("Dr Strange")
# print(marvel_avengers)

# marvel_avengers.pop()
# print(marvel_avengers)

# marvel_avengers.clear()
# print(marvel_avengers)

# marvel_avengers.sort()
# print(marvel_avengers)

# Tuples-Defining and Using Tuples
# A tuple is a collection of objects which are ordered and immutable. Tuples
# are sequences, just like lists. The differences between tuples and lists are,
# the tuples cannot be changed unlike lists and tuples use parentheses,
# whereas lists use square brackets.

# Tuples are identical to lists in all respects, except for the following properties:
# Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
# Tuples are immutable.

# t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
# t[2]= 'bark'
# print(t)

# t= (1,)
# print(type(t))

# t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
# print(t[-1])

# (s1, s2, s3, s4, s5, s6, s7)=t
# print(t)

# (s1, s2, s3, s4, s5, s6) = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
# print(s4)

# t= 1, 2, 3
# print(t)

# x1, x2, x3 = t
# print(x1, x2, x3)

# x1, x2, x3 = 4, 5, 6
# print(x1, x2, x3 )

# t = 2,
# print(t)

# Functions
# a function is a collection of code which performs a specific task. that is,
# a block of code which only runs when it is called.

# functions allow you to organize your code a lot better. they allow you to
# break up your code into different chunks that are doing different things.

# in python, we use the 'def' keyword when we want to declare a function.
# py will treat everything that comes after the ':' as our function block
# in order to write code that belongs to the block, we need to indent.

#  def hello_world(num):
#   return num * num * num

# print(hello_world(5))

# the code inside of the function will only get executed when we specify that we want to execute it.
# => invoking the function
# your functions shhould be named in lower case.

# if statements
# 'if' statements are a structure in python that allows us to help our programs make decisions
# by using 'if' statements, we could execute a certain part of our code if certain conditions are True.
# basically 'if' statements allow our programs respond to the input that they are given.

# 'if' statements are something even we humans deal with all the time. as you go through your day,
# you are executing 'if' statements.
# elif for elseif
# not() => negation

# yinka_is_cold = True
# yinka_is_not_cold = False
# yinka_is_shivering = False

# if yinka_is_cold:
#         print("The ac should be turned off but the windows open")
# elif yinka_is_not_cold:
#         print("The ac should be turned on but the windows closed")
# elif yinka_is_shivering:
#         print("The ac should be turned off and the windows shut")
# else:
#         print("I'm a hard working youth")

# a = 10
# b = 22
# c = 14

# if (a < b):
#         print("The value of a is less than b")
# else:
#         print("The value of a is greater than or equal to b")
        
# if (a < c):
#         print("The value of a is less than c")
# else:
#         print("The value of a is less than or equal to c")
        
# if (b < c):
#         print("The value of b is less than c")
# elif(b == c):
#         print("The value of b is equal to c")
# else:'
#         print("the value of b ic greater than c")
        

# collect input from users.. 1st and 2nd number
# user would input operator and py performs the calculation


# ops = input("Enter the operator: ")
# x = float(input("Enter the first number: "))
# y = float(input("Enter the second number: "))

# if(ops == "/"):
#         print(x / y)
# elif(ops == "*"):
#         print(x * y)
# elif(ops == "+"):
#         print(x + y)
# elif(ops == "-"):
#         print(x - y)
# else:
#         print("Get a calculator!!!")


                # Dictionaries
                
# a dictionary is a special structure in python which allows us to store informations in what is
# called Key:value pairs

#key:value

# month_conversions = {
#         "Jan": "January",
#         "Feb": "February",
#         "Mar": "March"
# }
        
# print(month_conversions.get("Feb"))
# print(month_conversions.get("Dec", "Not a valid key"))
# print(month_conversions)


# # Creating a Dictionary with Integer keys
# Dict = {1: "Geeks", 2: "For", 3: "Geeks"}
# print("\nDictionary with the use of integer keys: ")
# print(Dict)

# Creating a Dictionary with Mixed keys
# Dict = {"Name": "Geeks", 1: [1, 2, 3, 4, 5]}
# print("\nDictionary with the use of Mixed keys: ")
# print(Dict)

# creating an empty dictionary
# Dict = {}
# print("Empty Dictionary: ", Dict)

# Creating a Dictionary with a dict() method
# Dict = dict({1: "Geeks", 2: "For", 3: "Geeks"})
# print("\nDictionary with a dict() method")
# print(Dict)
        
# Creating a dictionary with each item as a pair
# Dict = dict([(1, "Geeks"), (2, "For"), (3, "Geeks")])
# print(Dict.get(2))

# Creating a nested dictionary
# Dict = {1: "Geeks", 2: "For", 3:{"A": "Welcome", "B": "to", "C": "Geeks"}}
# print(Dict[3]["A"])

# Creating an empty dictionary
# Dict = {}
# print("Empty Dictionary: ", Dict)

# Adding elements one at a time
# Dict[0] = "Geeks"
# Dict [2] = "For"
# Dict [3] = 1
# print("\nDictionary after adding three elements: ", Dict)

# Adding sets of values to a single key
# Dict["Value_set"] = 2, 3, 4
# print("\nUpdated key value: ", Dict)

# Adding Nested Key value to Dictionary
# Dict[5] = {"Nested" :{"1" : "Life", "2": "Geeks"}}
# print("\nAdding Nested Key: ", Dict)

# While loop
# a while loop is a structure in python that allows us to loop through and execute a block of code
# repeatedly until a certain condition is false.

# as long as the condition provided to the loop remains true, the loop continues to run in circles.
# It goes back to check the condition after each iteration.

# i = 1

# while i <= 14:
#         print (i)
#         i +=1
        
        
# print ("done looping")

# n = 5
# while (n > 0):
#         print(n)
#         n -= 1

# a = ["foo", "bar", "baz"]    
# while a:
#         print(a.pop(-1))
        
# a = [1, 2, 3, 4, 5]
# while a: 
#         print(a.pop())
        
# For loop
# a for loop is a special type of loop which allows us to loop over different collections of items.
# in for loops we specify a variable. this variable will represent a different value on each iteration
# each time, this variable will most likely have a different value
# for every letter in tsa, do something

# for letter in "TechStudio Academy":
        # print(letter)


# airlines = ["Air Peace", "Air France", "Emirates Airlines"]

# for airline in airlines:
#         print(airline)
        
# for index in range(12):
#         if index == 0:
#                 print("First iteration")
#         else:
#                 print("Not First")

# for x in range(3, 6):
#         print(x)
        
# for x in range(3, 8, 2):
#         print(x)

# for i in range(1, 4):
#         print(i)
# else:
#         print("No break\n")

# count = 0
# while True:
#         print(count)
#         count += 1
#         if count >= 5:
#                 break
        
# for x in range(1, 10, 2):
        # print(x)
        
# for x in range(10):
#         if x % 2 == 0:
#                 continue
#         print(x)

# count = 0
# while (count < 5):
#         print(count)
#         count += 1
# else:
#         print("count value reached %d" %(count))

# for i in range(1,10):
#         if(i%5 == 0):
#                 continue
#         print(i)

# print("List Iteration")
# l = ['geeks', 'for', 'geeks']
# for i in l:
#         print(i)
        
# print("Tuple \nIteration")
# t = ('geeks', 'for', 'geeks')
# for i in t:
#         print(i)
        
# print("\nString Iteration")
# s = 'Geeks'
# for i in s:
#         print(i)
        
# print("\nDictionary Iteration")
# d = dict()
# d['xyz'] = 123
# d['abc'] = 345
# for i in d:
#         print("% s % d" %(i, d[i]))

# for letter in 'geeksforgeeks':
#         if letter == "e" or letter == "s":
#                 continue
#         print("Current Letter: ", letter)

# for letter in 'geeksforgeeks':
#         if letter == 'e' or letter == 's':
#                 break
#         print("Current Letter", letter)

# for letter in 'geeksforgeeks':
#         pass
# print("Last Letter: ", letter)

# for i in range(10):
#         print(i, end = " ")

# l = [10, 20, 30, 40]
# for i in range(len(l)):
#         print(l[i], end = " ")
        
        
# sum = 0
# for i in range(1, 10):
#         sum = sum + i
#         print(sum, end = " ")

# for i in range(1, 10):
#         print(i)
# else:
#         print("No Break\n")

# 2D Lists and Nested loops

# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
# for r in T:
#         for c in T:
#                 print(c, end = " ")
#                 print()

# T.remove([2][2])

# for r in T:
#         for c in r:
#                 print(c, end =" ")
#         print()

# N = 5
# arr = [0] * N
# print(arr)

# N = 5
# arr = [0 for i in range(N)]
# print(arr)

# rows, cols = (5, 4)
# arr = [[0]*cols]*rows
# print(arr)

# N = 5
# arr = [[0 for i in range(cols)] for j in range(rows)]


# def translate(text):
#         translation = ""
#         for letter in text:
#                 if letter in "AEIOUaeiou":
#                         translation = translation + "m"
#                 else:
#                         translation = translation + letter
#         return translation
                
# print(translate(input("ENter any text: ")))


# there might be

# def divide(x, y):
#         try:
                # floor division: Gives only Fractional part as Answer
        #         result = x // y
        #         print("Yeah ! Your answer is :", result)
        # except ZeroDivisionError:
        #         print("Sorry ! You are dividing by zero ")

# Look at parameters and note the working of program
# divide(3, 0)

# Reading from an external file

# syllabus = open("syl.md", "r")

# syllabus = open("./TechStudio/syl.md", "a")

# syllabus.write("\n34=> Some Other stuffs")
# print(syllabus.read())
# print(syllabus.readlines())

# syllabus.close()

# pip install python-docx

# file = open("file.txt", "r")
# for each in file:
#         print(each)


# syllabus = open("file.txt", "r")
# print syllabus.read(5)

# file = open("Geek.txt", "w")
# file.write("This is the write command in Python. ")
# file.write("It allows to write in a particular file")
# file.close()

# file = open("sample.txt", "r")
# print(file.read())

# file.close()

# with open("Geek.txt") as file:
#         data = print(file.read())

# with open("Geek.txt", "r") as file:
#         data = file.readlines()
#         for line in data:
#                 word = line.split()
#                 print(word)

# with open("syl.md", "w") as file:
#         file.write("Hello World!!!")

# import num
# print(num.square(3))
# print(num.cube(3))

# import calc
# print(calc.add(10, 2))

# from math import sqrt, factorial
# print(sqrt(25))
# print(factorial(6))

# import random
# print(dir(random))

# import math

# print(sqrt(25))
# print(pi)
# print(math.degrees(4))
# print(radians(60))

# import random

# print(random.randint(0, 5))
# print(random.random() * 100)

# List = [1, 4, True, 800, "python", 27, "hello"]

# print(random.choice(List))

# import datetime
# from datetime import date
# import time

# print(time.time())

# print(date.fromtimestamp)

# import support
# support.print_func("Zara")

# Money = 2000
# def AddMoney():
        # Uncomment the following line to fix the code:
#         global Money
#         Money = Money + 1
        
# print(AddMoney)
# AddMoney()
# print(Money)

# fo = open("foo.txt", "wb")
# print("Name of the file: ", fo.name)
# print("Closed or not: ", fo.closed)
# print("Opening mode: ", fo.mode)
# print("Softspace flag: ", fo.softspace)