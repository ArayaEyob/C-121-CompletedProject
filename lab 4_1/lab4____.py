# #1
# f= open("readfile.txt",  "w")
# print("this line", file= f)
# print("this line 2", file = f)
# f.close()
# #2
import fileinput

file1 = open("temps.txt", 'r')
lines = file1.readlines()
file2 = open("ftemps.txt", 'w')

for i in range(len(lines)):
    cel = lines[i].strip()
    fahr = 9/5 * int(cel) +32,2
    file2.write(str(fahr)+ '\n')
file2.close()

