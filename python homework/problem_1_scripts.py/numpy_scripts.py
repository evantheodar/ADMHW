###1 Arrays
import numpy

def arrays(arr):
   
    return numpy.array(arr[::-1], float)
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

###2 Shape and Reshape
import numpy as np

def c(arr):
    # Convert the list of strings to a NumPy array of integers and reshape it to 3x3
    return np.array(arr, int).reshape(3, 3)

# Take input as space-separated integers
arr = input().strip().split(' ')
result = c(arr)
print(result)


###3 Transpose and Flatten
import numpy as np

n, m = map(int, input().split())

matrix = np.array([input().split() for _ in range(n)], int)

print(np.transpose(matrix))

print(matrix.flatten())


###4 Concatenate
import numpy as np
n, m, p = map(int, input().split())

array1 = np.array([input().split() for _ in range(n)], int)

array2 = np.array([input().split() for _ in range(m)], int)

result = np.concatenate((array1, array2), axis=0)

print(result)



###5 Zeros and Ones
import numpy as np
shape = tuple(map(int, input().split()))
print(np.zeros(shape, dtype=int))
print(np.ones(shape, dtype=int))



###6 Eye and Identity
import numpy

numpy.set_printoptions(legacy='1.13')

n, m = (map(int,input().split()))

print(numpy.eye(n, m, k=0))



###7 Array Mathematics 
import numpy as np

n, m = map(int, input().split())

A = np.array([input().split() for _ in range(n)], int)

B = np.array([input().split() for _ in range(n)], int)

add = A + B
subtract = A - B
multiply = A * B
floordivide = np.floor_divide(A, B)  # Integer division
mod = A % B
power = A ** B

# Print the results
print(add)
print(subtract)
print(multiply)
print(floordivide)
print(mod)
print(power)




###8 Floor, Ceil and Rint
import numpy as np

np.set_printoptions(legacy='1.13')

A = np.array(input().strip().split(), dtype=float)
print(np.floor(A))
print(np.ceil(A))
print(np.rint(A))



###9 Sum and Prod
import numpy as np


n, m = map(int, input().split())

array = np.array([input().split() for _ in range(n)], dtype=int)


sum_axis_0 = np.sum(array, axis=0)
product = np.prod(sum_axis_0)

print(product)



###10 Min and Max
import numpy as np

n, m = map(int, input().split())
 
array = np.array([input().split() for _ in range(n)], dtype=int)

min_values = np.min(array, axis=1)

max_of_mins = np.max(min_values)


print(max_of_mins)



###11 Dot and Cross
import numpy as np
N = int(input())
A = []
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)

B = []
for i in range(N):
    row = list(map(int, input().split()))
    B.append(row)


A = np.array(A)
B = np.array(B)
result = np.dot(A, B)  # or you can use A @ B

print(result)



###12 Inner and Outer
import numpy as np

A = np.array(list(map(int, input().split())))

B = np.array(list(map(int, input().split())))

inner_product = np.inner(A, B)

outer_product = np.outer(A, B)

print(inner_product)
print(outer_product)



###13 Polynomials
import numpy as np


coefficients = list(map(float, input().split()))

x = float(input())

result = np.polyval(coefficients, x)

print(result)



###14 Linear Algebra
import numpy as np

N = int(input())
A = []
for _ in range(N):
    row = list(map(float, input().split()))
    A.append(row)

A = np.array(A)

determinant = np.linalg.det(A)

print(round(determinant, 2))



###15 Mean, Var, and Std 
import numpy as np
n, m = map(int, input().split())
array = np.array([input().split() for _ in range(n)], dtype=int)
mean_values = np.mean(array, axis=1)
var_values = np.var(array, axis=0)
std_value = np.std(array)
print(mean_values)
print(var_values)
print(f"{std_value:.11f}")  # Print the standard deviation with 11 decimal places


