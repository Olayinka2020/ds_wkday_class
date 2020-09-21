# To determine if a word has two letters

# def Isogram():
#     Isogram = input("Enter a random word: ").lower()
#         Isogram = []
#     for letter in Isogram:
#         if letter in Isogram:
#                 print("The word is not an Isogram: ")
#         else:
#                 print("The word is not an Isogram")
#     return Isogram
                
# print(translate(input("ENter any text: ")))

def leap_year():
    year = int(input("Enter the year: "))
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print(" The year is a leap year:")
                        
    else:
        print("Not a leap year")
        
leap_year()

        