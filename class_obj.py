# classes and objects in python are extremely useful and can help 
# make ur code more organized and powerful.

# alot of times when we 're writing programs, we 're gonna have
# to work with differetn types of data and we have all sorts 
# of structures we can use to store that data, like lists, 
# dictionaries etc.

# however in the real world, not all kind of data can be 
# stored in a string or numbers.

# think of it like this, you can't represent a user of 
# ur app or even a person with numbers and strings alone.

# classes and objects allows us to create our own data-types

# A class is a blueprint for objects.

# let's model a university student

from student import Student

student1 = Student("Maoti", "50.0", "Science of Fraud", True)
student2 = Student("Maoti", "50.0", "Science of Fraud", True)
student3 = Student("Yinka", "50.0", "Science of Assasination", False)
student4 = Student("Tosin", "50.0", "Science of Talking", True)
student5 = Student("Fawaz", "50.0", "Science of checking temperature", True)

print(student1.gpa)