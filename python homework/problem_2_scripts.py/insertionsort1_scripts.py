



import math
import os
import random
import re
import sys


def insertionSort1(n, arr):
    # Step 1: Store the last element in the array
    key = arr[-1]
    
    # Step 2: Start from the second last element and move backwards
    i = n - 2
    
    # Step 3: Shift elements until we find the correct position for the key
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]  # Shift the element to the right
        print(" ".join(map(str, arr)))  # Print the current state of the array
        i -= 1
    
    # Step 4: Insert the key at its correct position
    arr[i + 1] = key
    print(" ".join(map(str, arr)))  # Print the final state of the array

# Example usage:
n = int(input())  # Size of the array
arr = list(map(int, input().split()))  # The array to be sorted

insertionSort1(n, arr)



