
1. Map and Lambda Function
# Function to generate the first N Fibonacci numbers
def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

# Define a cube function to cube each Fibonacci number
def cube(x):
    return x ** 3

