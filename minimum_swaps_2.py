import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    arr = [i-1 for i in arr]
    swaps = 0
    for i in range(len(arr)):
        if i != arr[i]:
            for j in range(len(arr) - i):
                if i == arr[j + i]:
                    k = arr[i]
                    arr[i] = arr[j + i]
                    arr[j + i] = k
                    swaps += 1
    return swaps

arr = [4,3,1,2]

print(minimumSwaps(arr))
