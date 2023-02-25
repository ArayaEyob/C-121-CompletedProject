#1
for i in range(5):
    print("Hello, My name is Araya")
#a
for i in range(3):
    num = eval(input("Enter a number: "))
    print('the square of your number is', num  **2)
print("the loop is now done")
#b
for i in range(5, 0, -1):
    print(i, end = '')
print('blast off !!!', end = '')


for i in range(5):
    print('*' * (i +1))

from random import randint

num = randint(1,10)
guess = input('Enter your guess: ')
if guess == num:
    print('you got it')
else:
    print("sorry the is", num )
