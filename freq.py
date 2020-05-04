def freqQuery(queries):
    q_dict = {}
    arr = []
    for i in range(len(queries)):
        if queries[i][0] == 1:
            if queries[i][1] in q_dict:
                q_dict[queries[i][1]] += 1
            else:
                q_dict[queries[i][1]] = 1
        elif queries[i][0] == 2:
            if queries[i][1] in q_dict:
                q_dict[queries[i][1]] -= 1
        else:
            if queries[i][1] in q_dict.values():
                arr.append(1)
            else:
                arr.append(0)
    return arr

queries = [
    [1,89],
    [3,15],
    [1,12],
    [1,47],
    [1,23]
]

print(set(queries))
