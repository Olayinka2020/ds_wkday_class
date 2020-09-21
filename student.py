

class Student:
    def __init__(self, name, gpa, major, is_on_probation):
        self.name = name
        self.gpa = gpa
        self.major = major
        self.is_on_probation = is_on_probation
        
    def is_first_class(self):
        if self.gpa >= 20.0:
            
        