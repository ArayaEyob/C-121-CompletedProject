# 1 LIST OF L AND RANDOM NUMBER
import random

L = []
count = 0
print("random integers between 0 and 10:")
for num in list(range(1, 51)):
    rand = random.randrange(10)
    sq = rand ** 2
    L.append(sq)
print(L)

for i in L:
    if i > 50:
        count += 1
print('the total num greater than 50 is', count)

# 2 QUIZ GAME
questions = ['What is the capital of France?', 'What is the longest river in the United States?',
             'Which state has only one neighbor?']
answers = ['Paris', 'Mississippi Missouri', 'Maine']
count = 0
for i in range(len(questions)):
    print(questions[i])
    guess = input("enter your answer :")
    if guess.lower() == answers[i].lower():
        print('correct')
        count += 1

    else:
        print('wrong')
        print(answers[i])
print(count, "answers are correct")

# 3
import string

count = 0
word = input("enter a sentence: ")
for i in word:
    if i in string.punctuation:
        count += 1
print(count)

# f

from random import choice

name = ['ben', "mark", "john", "hammad", "eric"]
new = choice(name)
print(new)

# G
from random import sample

name1 = ['ben', "mark", "john", "hammad", "eric"]
print(sample(name1, 0))
# h

s = "random statement:LOJSDFNSIDFNDFIJSBCKJXC,ZM MZDSKAB VZMBIZKSNVJBZKBIAKBOSXBVOZBXCB "
for i in range(20000):
    print(choice(s), end="")
# i
from random import shuffle

players = ['messi', "cr7", " jesus", "james", " phil", " hurt"]
shuffle(players)

print(players)

# j
from random import shuffle

team1 = ["messi", "cr7", "silva", "jones"]
team2 = ["neymar", "di maria", "salah", ]

shuffle(team1 + team2)
print(team1 + team2)