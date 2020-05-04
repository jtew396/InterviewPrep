import math

def bubblesort(arr):
    isSorted = False
    lastUnsorted = len(arr) - 1
    while not isSorted:
        isSorted = True
        for i in range(lastUnsorted):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
                isSorted = False
        lastUnsorted -= 1
    return arr

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


arr = [6,7,3,2,1,9,4]

print(bubblesort(arr))
