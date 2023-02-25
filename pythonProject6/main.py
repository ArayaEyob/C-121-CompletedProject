# decimal = input("enter a decimal integer:")
# if decimal == 0:
#     print(0)
# else:
#     print("quotient Remainder Binary")
#     bitstring = ''
#     while decimal > 0:
#         remainder = decimal % 2
#         decimal = decimal //2
#         bitstring = str(remainder) + bitstring
#
#         print("%5d%8d%12s") % (decimal, remainder, bitstring))
#
#     print(bitstring)
#


# sen = input("enter a sentence: ")
#
# listofwords = sen.split()
# print((listofwords))
#
# data = "python Rules"
#
# n = data.endswith("i")
# m = "totally". join(data.split())
# print(m)

lyst = [10, 20, 30]


# def mean(lyst):
#     if len(lyst) == 0:
#         return 0
#     list.sort()
#     total = 0
#     for number in list:
#         total += number
#     return total / len(list)
#
# def main():
#     print("mean of [10,20,30]: ", mean(list))
#
# main()

def odd(n): return n % 2 == 1
print(list(filter(odd, range(10))))