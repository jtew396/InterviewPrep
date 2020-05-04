def rotateMatrix(arr):

    new_arr = []
    for i in range(len(arr)):
        temp_arr = []
        for j in range(len(arr)):
            temp_arr.append(0)
        new_arr.append(temp_arr)

    print(new_arr)

    for i in range(len(arr)):
        for j in range(len(arr)):
            new_arr[j][i] = arr[i][j]

    return new_arr


arr = [[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]]

print(rotateMatrix(arr))
