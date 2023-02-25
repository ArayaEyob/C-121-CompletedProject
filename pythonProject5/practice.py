fileName = input("enter the filename:")
f = open(fileName, "r")
number = []
for line in f:
    words = line.split()
    for word in words:
        number.append(float(word))
print(number)

number.sort()
mid_value = len(number) // 2
print("the median is", end = "")

if len(number) % 2 == 1:
    print(number[mid_value])
else:
    print(number[mid_value] + number[mid_value - 1] /2)