# QuickSort Algorithm 1

def solution(arr):
    quicksort(arr, 0, len(arr) - 1)
    return arr

def quicksort(arr, left, right):
    if (left >= right):
        return
    pivot = arr[(left + right) // 2]
    index = partition(arr, left, right, pivot)
    quicksort(arr, left, index - 1)
    quicksort(arr, index, right)

def partition(arr, left, right, pivot):
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left #Return the partition point

arrTest1 = [17, 41, 5, 22, 54, 6, 29, 3, 13]

print(solution(arrTest1))
