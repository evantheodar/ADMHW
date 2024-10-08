

###1 Say "Hello, World!" With Python
world = "Hello, World!"
print(world)



###2 Python If-Else
n = int(input())
if n % 2 == 1:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")


###3 Arithmetic Operators
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)


###4 Python: Division
a = int(input())
b = int(input())
print(a//b)
print(a/b)


###5 Loops
n = int(input())

for i in range(n):
    print(i ** 2)


### 6 Write a function
def is_leap(n):
    leap = False
    if n%4==0:
        leap=True
        if n%100==0:
            leap=False 
            if n%400==0:
                leap=True
    else:
        leap=False
    return leap


###7 Print Function
from __future__ import print_function

N = int(input())
print(*range(1,N+1), sep='')


