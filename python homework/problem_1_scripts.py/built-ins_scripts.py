
###1 Zipped!
N, X = map(int, input().split())
marks = [list(map(float, input().split())) for _ in range(X)]
for student_marks in zip(*marks):
    print(f"{sum(student_marks) / X:.1f}")


###2 Athlete Sort.
import math
import os
import random
import re
import sys
 
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

k = int(input())

arr.sort(key=lambda x: x[k])

for row in arr:
    print(*row)



###3 ginortS
S = input()

lowercase_letters = []
uppercase_letters = []
odd_digits = []
even_digits = []

for char in S:
    if char.islower():
        lowercase_letters.append(char)
    elif char.isupper():
        uppercase_letters.append(char)
    elif char.isdigit():
        if int(char) % 2 == 0:
            even_digits.append(char)
        else:
            odd_digits.append(char)

lowercase_letters.sort()
uppercase_letters.sort()
odd_digits.sort()
even_digits.sort()

result = ''.join(lowercase_letters + uppercase_letters + odd_digits + even_digits)

print(result)

