from math import sqrt

a, b, c = map(float, input().split())

x = a**5 - 2*sqrt(abs(b)) + a*b*c

print(format(x, '.2f'))
