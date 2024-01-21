def count_negatives(arr, k):
    lst = []
    start = 0
    count = 0

    for i in range(len(arr)):
        if arr[i] < 0:
            count += 1
        if i - start + 1 == k:
            lst.append(count)
            if arr[start] < 0:
                count -= 1
            start += 1
    return lst


arr = [-1, 2, -2, 3, 5, -7, -5]
k = 3
print(count_negatives(arr, k))
