#1

A = int(input("enter a value for 'A': "))
B = int(input("enter a value for 'B': "))
print("")
lyst = []

for i in range(A):
    innerlist = []
    for j in range(B):
        innerlist.append(i * j)
    lyst.append(innerlist)

print(lyst)
# 2

lyst1 = [10, 21, 4, 45, 66, 93, 1]
even_count, odd_count = 0, 0
for num in lyst1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("the even numbers in the list:", even_count)
print("the odd number in the lsit:", odd_count)

# #3

Lisst = [[j, k] for i in range(1) for j in range(1) for k in range(2)]
print(Lisst)

# 4
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("\nsquare every number in the said list: ")

square_Num = list(map(lambda x: x ** 2, num))
print(square_Num)
print("\nCube every number of the said list: ")
cube_num = list(map(lambda x: x ** 3, num))
print(cube_num)

# 6
import random

list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", ",j", "q", "k"]
dict = {}
suit = ['heart', 'flower', 'spear', 'diamond']
for i in suit:
    dict[i] = list
# for i in dict:
#     print(i,"-",dict[i][random.randint(0,12)])
A = suit[random.randint(0, 4)]
print(A, dict[A][random.randint(0, 12)])

# 6
from functools import reduce

def add(x, y): return x + y
lyst2 = ["chickfila", "burger", " bread"]
lyst3 = ["pepsi,", "cuppioncino", "milk"]

foodanddrink = reduce(add, lyst2 + lyst3)
print(foodanddrink)
# a
def square(x):
    return x * x


lyst4 = [1, 4, 6, 8]
lyst4 = list(map(square, lyst4))
x = [1, 4, 6, 8]
print(lyst4)

# b
num1 = [1, 3, 5]
num2 = [4, 6, 8]
result = list(map(lambda x, y: x + y, num1, num2))
print(result)

# c
words = ["j", "k", "m"]
result = map(list, words)
print(list(result))
# d
def abs(x):
    return x > 0

numbers = [-9, -4, 0, -1, 2, 9, 8, -8, 7, 4]
sq = filter(abs, numbers)
print(list(sq))
