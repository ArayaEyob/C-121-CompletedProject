dict = {"brand": "ford", "model": "mustang", "year": }
print(dict.items())
#print the whole keys and values in dictionary

print(dict.keys())
#print the keys in a dictionary

print(dict.values())
#print the keys in a dictionary

print(dict["brand"])
#print a value in a specific key

# note, we cant access a value specifically

name = {"red": 1}
newdict = {'orange': 2, "yellow": 3}

name.update(newdict)
#prints the updated name

A = ['f.name'].append('lastname')
# Adds a new list in the previse list

A = {'red': 1}
# Adds an integer in a dict
print(A['red'] + 3)
#
#
#

def rec(x):
    print(x)
    if x == 0:
        return x
    print(x)
    return rec(x -1)

print(rec(0))




#countup

def rec(e, s =0)
    print(s)
    if s == e:
        return
    rec(e,s + 1)
rec(11)