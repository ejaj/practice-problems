def min_nax_diff(arr, k):
    n = len(arr)
    window_sum = sum(arr[:k])
    average_sum = window_sum / k
    max_sum = average_sum
    min_sum = average_sum
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        average_sum = window_sum / k
        max_sum = max(average_sum, max_sum)
        min_sum = min(average_sum, min_sum)
    return max_sum - min_sum


arr = [3, 8, 9, 15]
k = 2
print(min_nax_diff(arr, k))
