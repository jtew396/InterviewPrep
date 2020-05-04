# Cracking the Coding Interview
# Binary Search Algorithm

# Iterative Binary Search Algorithm
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) / 2
        if arr[mid] < x:
            low = mid + 1
        elif a[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1   # Error

# Recursive Binary Search Algorithm
def binarySearchRecursive(arr, x, low, high):
    if low > high:
        return -1   # Error

    mid = low + ((high - low) / 2)
    if arr[mid] < x:
        return binarySearchrecrusive(arr, x, mid + 1, high)
    elif arr[mid] > x:
        return binarySearchRecursive(arr, x, low, mid - 1)
    else:
        return mid
