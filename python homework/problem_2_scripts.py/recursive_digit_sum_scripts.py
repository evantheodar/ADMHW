#!/bin/python3

import math
import os
import random
import re
import sys


def superDigit(n, k):
    # Helper function to compute the recursive super digit
    def recursive_super_digit(x):
        if len(x) == 1:
            return int(x)
        else:
            # Recursively call on the sum of the digits
            return recursive_super_digit(str(sum(map(int, x))))
    
    # Calculate the sum of digits of n and multiply by k
    initial_sum = sum(map(int, n)) * k
    
    # Call the recursive function on the result
    return recursive_super_digit(str(initial_sum))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

