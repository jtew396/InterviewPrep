# QuickSort Algorithm 2
# QuickSort is recursive
# Divide-and-Conquer algorithm
# Very efficient for large data sets
# Worst case is O(n^2)
# Average case is O(nlogn)
# Performance depends largely on Pivot selection

def quick_sort(arr):
    quick_sort2(arr, 0, len(arr) - 1)
    return arr

def quick_sort2(arr, left, right):
    print("The Quick Sort 2: " + str(arr))
    if left < right:
        pivot = partition(arr, left, right)     # Gather the pivot by calling partition
        quick_sort2(arr, left, pivot - 1)       # Pass in items left of pivot
        quick_sort2(arr, pivot + 1, right)      # Pass in items right of pivot
    return arr

def get_pivot(arr, left, right):
    mid = (left + right) // 2                   # Get a mid index
    pivot = right                               # Set pivot equal to right index
    if arr[left] < arr[mid]:                    # If the value at the low index is less than the valuea the mid index
        if arr[mid] < arr[right]:
            pivot = mid
    elif arr[left] < arr[right]:
        pivot = left
    print("The pivot is: " + str(pivot))
    return pivot

def partition(arr, left, right):
    pivotIndex = get_pivot(arr, left, right)
    pivotValue = arr[pivotIndex]
    arr[pivotIndex], arr[left] = arr[left], arr[pivotIndex]
    border = left

    for i in range(left, right + 1):
        if arr[i] < pivotValue:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]
            print(arr)
    arr[left], arr[border] = arr[border], arr[left]
    print(arr)
    print("The border is: " + str(border))
    return border

arrTest1 = [17, 41, 5, 22, 54, 6, 29, 3, 13]

print(quick_sort(arrTest1))
