def min_sum(arr, k):
    window_sum = sum(arr[:k])
    minimun_sum = window_sum
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        minimun_sum = min(window_sum, minimun_sum)
    return minimun_sum

def min_sum_another_way(arr, k):
    window_sum = 0
    min_sum = float("inf")
    start = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if (i - start + 1 == k):
            min_sum = min(min_sum, window_sum)
            window_sum -= arr[start]
            start += 1
    return min_sum


arr = [10, 4, 2, 5, 6, 3, 8, 1]
k = 3

print(min_sum_another_way(arr, k))
