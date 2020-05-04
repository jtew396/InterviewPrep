# Cracking the Coding Interview
# Quick Sort Algorithm

def quickSort(arr, left, right):
    index = partition(arr, left, right)
    if left < index - 1:                    # Sort the left half
        quickSort(arr, left, index - 1)
    if index < right:                       # Sort the right half
        quickSort(arr, index, right)


def partition(arr, left, right):
    pivot = arr[left + (right - left) / 2]  # Pick pivot point
    while left <= right:
        # Find element on left that should be on right
        while arr[left] < pivot:
            left += 1

        # Find element on right that should be on left
        while arr[right] > pivot:
            right += 1

        if left <= right:
            swap(arr, left, right)  # Swaps elements
            left += 1
            right -= 1

    return left
