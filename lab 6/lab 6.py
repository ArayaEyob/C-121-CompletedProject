num = [3,1,7,1,4,10]
num.sort
midpoint = len(num) // 2
print('Median: ', end = " ")

if len(num) % 2 == 1:
    print(num[midpoint])
else:
    print(num[midpoint] + num[midpoint -1] / 2)

import numpy
from scipy import stats
lyst = [3,1,7,1,4,10]
x = numpy.median(lyst)

print("Median: ", x)

x = numpy.mean(lyst)

print("Mean:", x)

x = stats.mode(lyst)

print("Mode:", x)