# 1
file = open("readfile.txt", "r")
data = file.read()
file.close()

print(data)

#2

file1 = open('temps.txt', 'r')
lines = file1.readlines()
file2 = open('ftemps.txt', 'w')
for i in range(len(lines)):
    c = lines[i].strip()
    f = round((float(c)*1.8)+32, 2)
    file2.write(str(f) + " F " + "\n")
file2.close()

# 3
str = ' ArayaLemma '
reverse_string = ''
count = len(str)
while count > 0:
    reverse_string += str[count - 1]
    count = count - 1
print(reverse_string)
