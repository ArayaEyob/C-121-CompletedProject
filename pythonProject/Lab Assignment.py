#question 1 Tempreture 

tempreture = eval(input("Enter your temprature: "))
unit = input(" (C)celsius or (F)fahrenheit: ")
if unit.upper() == "C":
    converted = 9/5 * tempreture + 32
    print(f"the temprature is {converted} fahrenheit")
else:
    converted = 5/9 * (tempreture - 32)
    print(f"the temprature is {converted} celsius")

# question 2 Average calculation
number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a second number: "))
print("The average is", (number_1 + number_2 / 2))

#question 3 practice
print('3+4')
print('the value of 3+4 is, 3+4')