# 1

gym = {"name": "john", "age": 25, "gender": "male", "occupation": "Student"}

# prints the value in the key called "age"
print(gym["age"])

# print each value in the dic
print(gym.items())

# convert the dictionary into tuples
lyst = []
for k, v in gym.items():
    lyst.append((k, v))
print(lyst)

# print the sorted list

lyst.sort()
print("Sorted list", lyst)


# 2

def rec(x):
    print(x)
    if x == 0:
        return x
    print(x)
    return rec(x - 1)


print(rec(0))


# count up

def rec(e, s=0):
    print(s)
    if s == e:
        return
    rec(e, s + 1)

rec(15)


# 3

def poly(x):
    return x ** 3 + 2 * x - 1


num = map(poly, (1, 2, 3, 4))
print(num)
for i in num:
    print(i)

# 5

my_list = [1, 2, 3, 6, 9, 13, 12, 15, 16, 18, 19, 21, 24, 26]
new_list = list(filter(lambda x: (x % 3 == 0), my_list))
print(new_list)

# 6
from functools import reduce


def minimum(a, b):
    return a if a < b else b


def maximum(a, b):
    return a if a > b else b


num = [1, 3, 5, 2, 4]
print('the minimum in the list is', reduce(minimum, num))
print('the maximum in the list is', reduce(maximum, num))
