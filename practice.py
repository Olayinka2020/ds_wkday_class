#   Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum

# a = int(input("First integer: "))
# b = int(input("Second integer: "))
# product = (a * b)
# sum = (a + b)

# if(product <= 1000):
#         print(product)
# else:
#         print("The product is more than 1000, hence the sum is: ", sum)



# def hello_world(num):
#      return num * num * num

# print(hello_world(5))

# Create a function that can accept two arguments name and age and print its value

# def demo(name, age):
#         return name, age
        
# print(demo('Yinka', 27))

# def adder(x, y):
#     return x + y

# print(adder(5, 3))

# Define a function that converts from temperatures in Fahrenheit to temperatures in Kelvin, and another function that converts back again.

# def Kelvin(fah):
#     return (fah - 32) * (5/9) + 273.15

# print(Kelvin(75))

# def cal(a, b):
#         return a + b, a - b

# print(cal(5, 6))

# def func1(args):
#         for arg in args:
#                 print(arg)
        
# def emp(name, salary):
#         return name, salary
# if(salary == 0 ):
#         print(9000)
# elif print(emp("Yinka", 10000)):
# else:
#         print(name, salary)

# Question 1: Print First 10 natural numbers using while loop

# i = 1
# while (i <= 10):
#         print(i, end = " ")
#         i += 1
        
# for i in range (1, 6):
#         print(i, len(i), end = " ")
#         print()

# x = int(input("Enter a number: "))
# sum = 0
# for i in range(1, x + 1, 1):
#         sum = sum + i
# print("\n")
# print( sum)
        
# sum1 = 0
# n = int(input("Please enter number "))
# for i in range(1, n + 1, 1):
#     sum1 += i
# print("\n")
# print("Sum is: ", sum1)

#6 x = input("Enter a number: ")
# print(len(x))

# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

# for i in list1:
#         if i <= 150 and i % 5 == 0:
#                 print(i)
       

# list1 = [10, 20, 30, 40, 50]
# list1.reverse()
# print(list1)

# x = int(input("Enter a number: "))

# i = 1
# while  i <= 12:
#         product = x * i
#         i += 1
#         print(product, end =" ")
        
# i = 1
# while i <= 4:
#         print("Hello World")
#         i += 1
    
#    x, y = 2, 6
# x, y = y, x + 2
# print(x, y)

# x = '''This is a multiline
# string
# written in 
# three liness'''
# print(x)

# x = 0
# y = 0
# def incr(x):
#     y = x + 1
#     return y
# incr(5)
# print(x, y)

# pi = 3.14
# def area (r):
#     return pi * (r * r)

# print(area(6))

# numcalls = 0
# def square (x):
#     global numcalls
#     numcalls = numcalls + 1
#     return x * x

# print(square(6))

# x = 1
# def f():
#     return x
# print(x)
# print(f())

# def count_digits(x):
#     return len(x)
# print(count_digits(6567))

# x = int(input("Enter the first integer: "))
# y = int(input("Enter the second integer: "))
# product = x * y
# sum = x + y

# if product < 1000:
#     print(product)
    
# else:
#     print("The product is greater than 1000, so the sum is: ", sum)
    
# def pro_sum(x, y):
#     product = x * y
#     sum = x + y
#     if product <= 1000:
#         return product
#     else:
#         return sum
# print(pro_sum(123, 34))

# def removechars(str, n):
#     return str[n:]

# print("Removing n number of chars")
# print(removechars("pynative", 4))

# def isfirst_and_last_same(numberlist):
#     print("Given list is ", numberlist)
#     firstElement = numberList[0]
#     lastElement = numberlist[-1]
    
#     if firstElement == lastElement:
#         return True
#     else:
#         return False
    
#     numList = [10, 20, 30, 40, 10]
#     print("The result is: ", isfirst_and_last_same(numList))

# list = [10, 20, 33, 46, 55]

# for i in list:
#     if i % 5 == 0:
#         print (i)
    
# for num in range (10):
#     for i in range (num):
#         print (num, end = " ")
#     print("\n")
    
# num = 121
# if 

# for i in range (1, 11):
#     for j in range (1, 11):
#         print(i * j, end = " ")
#     print("\t\t")