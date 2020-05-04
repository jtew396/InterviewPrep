def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    arr = []
    cash = k
    count = 0
    for i in sorted_prices:
        if i < cash:
            count += 1
            cash -= i
            arr.append(i)
    print(arr)
    return count

arr = [1,2,3,4]
k = 7

print(maximumToys(arr, k))
