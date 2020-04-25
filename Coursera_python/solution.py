import sys
"""
a = int(sys.argv[1]) 
b = int(sys.argv[2]) 
c = int(sys.argv[3])
x1 = x2 = 0
d = (b ** 2) - (4 * a * c)

if d == 0:
    x1 = x2 = - (b/2*a)
elif d > 0:
    x1 = (-b + (d ** 0.5))/(2*a)
    x2 = (-b - (d ** 0.5))/(2*a)

print(int(x1))
print(int(x2))
"""

def func(num):
    return(str(num))
print(list(map(func, range(0, 5))))
