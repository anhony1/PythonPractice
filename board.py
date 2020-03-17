import time
import random

wordlist = ["Thomas", "Games", "Jupiter", "Javascript", "Coronavirus", "Waiting", "Superman", "PythonisAwesome",
            "TypingChallenge", "supercalifragilisticexpialidocious"]

theword = random.choice(wordlist)

print("Welcome to the tpying challenge! Start the game by typing the word and the timer begins!")
print("Your word is: ", theword)

print("Type the word to begin. First word doesn't count but next 5 do!")

choice = 0
word = input()
seconds = time.time()

while choice != 5:
    print("Type the word:")
    word = input()
    if theword == word:
        choice += 1
    else:
        print("Incorrect INPUT RETYPE!")

seconds2 = time.time()

result = seconds2 - seconds

print("It took you " + str(round(result, 2)) + " seconds to type " + word + " 5 times!")
