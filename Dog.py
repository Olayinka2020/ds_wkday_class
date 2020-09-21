class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
    buddy  = Dog("Buddy", 10)
    
    print(buddy.age)
    
    