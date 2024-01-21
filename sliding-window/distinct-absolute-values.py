def count_distinct(arr):
    count = 0
    d = {}
    for item in arr:
        if item >= 0 and item not in d:
            d[item] = 1
            count += 1
    return count


arr = [-1, -1, 0, 1, 1, 1]
print(count_distinct(arr))
