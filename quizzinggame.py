import json
import requests
import random
import html

print("WELCOME TO THE QUIZ GAME!")

print("Would you like to play?")
answer = input()

if answer == 'yes':
    playerstillwantstoplay = 'yes'
else:
    playerstillwantstoplay = 'no'

print("Let us begin Random Questions")
while playerstillwantstoplay == 'yes':

    quiz = requests.get("https://opentdb.com/api.php?amount=10&type=multiple")
    data = json.loads(quiz.text)

    question_asked = data['results'][0]['question']
    answers = data['results'][0]['incorrect_answers']
    correct_answer = data['results'][0]['correct_answer']
    answers.append(correct_answer)
    random.shuffle(answers)

    print(html.unescape(question_asked) + "\n")
    correct_answered = 0
    for answer in answers:
        print(html.unescape(answer))

    user_answer = input()
    if user_answer == correct_answer:
        print("CORRECT ANSWER!")
        correct_answered += 1
    else:
        print("Incorrect answser")

    print("Continue playing? Yes or No?")

    response = input()

    if response == 'no':
        break

print("Thanks for playing!")
