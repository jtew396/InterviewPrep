import math
import os

def someFunction(i):
    if i == 0:
        return 0
    else:
        return 2 * someFunction(i - 1) + i * i

print(someFunction(4))
