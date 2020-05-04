def makeAnagram(a, b):
    a_dict = {}
    delete_count = 0
    for i in a:
        if i not in a_dict:
            a_dict[i] = 1
        else:
            a_dict[i] += 1
    for j in b:
        if j not in a_dict:
            delete_count += 1
        elif a_dict[j] <= 0:
            delete_count += 1
        else:
            a_dict[j] -= 1
    for k in a_dict:
        if a_dict[k] > 0:
            delete_count += a_dict[k]
    return(delete_count)

a = "showman"
b = "woman"

print(makeAnagram(a,b))
