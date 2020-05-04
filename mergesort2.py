# Cracking the Coding Interview - Merge Sort
# Runs in O(nlogn) runtime

def solution(arr):
    helper = arr                                    # Declare a helper array
    mergesort(arr, helper, 0, len(arr) - 1)
    return arr

def mergesort(arr, helper, low, high):
    if low < high:
        middle = low + (high - low) // 2
        mergesort(arr, helper, low, middle)         # Sort the left half
        mergesort(arr, helper, middle + 1, high)    # Sort the right half
        merge(arr, helper, low, middle, high)       # Merge them

def merge(arr, helper, low, middle, high):
    # Copy both halves into a helper array
    for i in range(low, high + 1):
        helper[i] = arr[i]

    helperLeft = low
    helperRight = middle + 1
    current = low

    # Iterate through helper array. Compare the left and right half, copying back
    # the smaller element from the two halves into the original array
    while helperLeft <= middle and helperRight <= high:
        if helper[helperLeft] <= helper[helperRight]:
            arr[current] = helper[helperLeft]
            helperLeft += 1
        else:   # If right element is smaller than the left
            arr[current] = helper[helperRight]
            helperRight += 1
        current += 1

    # Copy the rest of the left side of the array into the target array
    remaining = middle - helperLeft
    for i in range(remaining + 1):
        arr[current + i] = helper[helperLeft + i]



if __name__=='__main__':
    arr = [1, 4, 5, 2, 8, 9]
    print(solution(arr))
