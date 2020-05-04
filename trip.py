def countTriplets(arr, r):
    arr_set = set(arr)
    arr_of_arr = []
    count = 0

    for i in range(len(arr)):
        arr_of_arr.append([arr[i],arr[i]*r,arr[i]*r*r])

    for j in arr_of_arr:
        if j[0] in arr_set and j[1] in arr_set and j[2] in arr_set:
            count += 1
    print(arr_of_arr)
    return count

arr1 = [1, 5, 5, 25, 125]
r1 = 5
print(countTriplets(arr1, r1))


Beach club - unwich
no tomattoes, no cheese
