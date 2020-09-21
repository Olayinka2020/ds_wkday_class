# the idea is that we'll have a secret word that we store inside of our program and then the user
# will interact with the program to try and guess the secret word

# we want the user to be able to keep guessing what the secret word is until they finally get the word.

secret_word = "hello"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

# while (guess != secret_word):
#     guess = input("Enter guess: ")
#     guess_count += 1
# print("You win!!!")

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        
# when we break this loop, there's going to be 2 possible scenarios. it's either the user guesses
# the word correctly or the user runs out of guesses

if out_of_guesses:
    print("You re out of guesses and you lost the game")
else:
    print("You win!!")