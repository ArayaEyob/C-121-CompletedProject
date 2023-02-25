#1
count = 0
for i in range(1,101):
    if str(i **2)[-1] == str(4):
        count +=1
print(count)


#2
largest = int(input("Enter a positive number: "))
for i in range(4):
    num = int(input("Enter a positive number: "))
    if (num > largest):
        largest = num
print(largest)

#4
result =  ""
user_input = input("enter a sentence: ")
vowels = "AaEeIiOoUu"
for i in user_input:
    if i in vowels:
        result += i
print(result)

#5
name = input("enter a text: ")
for i in range(len(name)):
    if name[i] == "a":
        print(i)

#6

user = input("enter a string:")
if user[0].isalpha() == True:
    print("your string starts with a letter ")
else:
    print("your string does not start with a letter")



