# 1

n = int(input("enter a number:"))

if n % 5 == 0 and n % 7 == 0:
    print(n, 'is the multiple of 5 and 7')
else:
    print(n, 'is not the mulitple of 5 and 7')

# 2
n = int(input("enter a number: "))
rev = 0

while (n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10

print(rev)


# 3

def getsum(num):
    sum1 = 0
    while num != 0:
        sum1 = sum1 + (num % 10)
        num = (num // 10)

    return sum1


num = int(input("enter a number: "))
print(getsum(num))

# 4

list = []
for i in range(100, 201):
    i = str(i)
    sum = 0
    for j in i:
        j = int(j)
        sum = sum + j
    if sum % 2 == 0:
        list.append(i)
print('All Integers Within The Range 100-200 Whose Sum Of Digits Is An Even Number is =', list)

# 5



inputlist = ["araya", "matt", "aki", "aidan"]
index = 1
del inputlist[index]
print(inputlist)

# 6

year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(format(year))

elif (year % 4 == 0) and (year % 100 != 0):
    print(format(year))

else:
    print("{} is not a leap year".format(year))

# 7

dic = {"matt": 19, "araya": "cs", "cody": 20}
for keys, value in dic.item():
    print(keys)
    print(value)
