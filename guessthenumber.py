import random

answer = random.randint(0, 20)

print("The number is", answer)

i = 0

while i == 0:
    print("Guess a number")
    number = int(input())

    if answer == number:
        print("Correct!")
        break
    elif answer < number:
        print("Lower")
    elif answer > number:
        print("Higher")
