# MergeSort Algorithm 1

def solution(arr):
    tmp = [0] * len(arr)
    mergeSort(arr, tmp, 0, len(arr) - 1)
    return

def mergeSort(arr, temp, leftStart, rightEnd):
    if leftStart >= rightEnd:
        return
    middle = (leftStart + rightEnd) // 2
    # print("Left Start: " + str(leftStart) + " | Right End: " + str(rightEnd))
    mergeSort(arr, temp, leftStart, middle)
    mergeSort(arr, temp, middle + 1, rightEnd)
    mergeHalves(arr, temp, leftStart, rightEnd)

def mergeHalves(arr, temp, leftStart, rightEnd):
    leftEnd = (rightEnd + leftStart) // 2
    rightStart = leftEnd + 1
    size = rightEnd - leftStart + 1

    left = leftStart
    right = rightStart
    index = leftStart

    while left <= leftEnd and right <= rightEnd:
        if arr[left] <= arr[right]:
            temp[index] = arr[left]
            left += 1
        else:
            temp[index] = arr[right]
            right += 1
        index += 1
    # print("Copy from arr: " + str(arr) + " | Starting from Left index: " + str(left) + " | into temp: " + str(temp) + " | starting at index: " + str(index) + " | # elements: " + str(leftEnd - left + 1))
    # print("Copy from arr: " + str(arr) + " | Starting from Righ indext: " + str(right) + " | into temp: " + str(temp) + " | starting at index: " + str(index) + " | # elements: " + str(rightEnd - right + 1))
    # print("Copy from temp: " + str(temp) + " | Starting from Left index: " + str(leftStart) + " | into arr: " + str(arr) + " | starting at index (LeftStart): " + str(leftStart) + " | # elements: " + str(len(arr)))

# arr = [10, 5, 2, 7, 4, 9, 12, 1, 8, 6, 11, 3]

arr = [1, 4, 5, 2, 8, 9]
solution(arr)
print(arr)
