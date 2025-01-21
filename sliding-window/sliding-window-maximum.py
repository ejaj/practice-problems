from collections import deque


def window_maximum_recompute(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return []  # Handle invalid inputs
    result = []
    n = len(arr)
    window_max = max(arr[:k])
    result.append(window_max)
    for i in range(1, n - k + 1):
        window_max = max(arr[i:i + k])
        result.append(window_max)
    print(result)


def window_maximum_reuse(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return []  # Handle invalid inputs

    result = []
    n = len(arr)

    # Compute the maximum for the first window
    window_max = max(arr[:k])
    result.append(window_max)

    # Slide the window
    for i in range(1, n - k + 1):
        if arr[i - 1] == window_max:
            window_max = max(arr[i:i + k])
        else:
            new_value = arr[i + k - 1]
            window_max = max(window_max, new_value)
        result.append(window_max)
    print(result)


def window_maximum_deque(arr, k):
    if not arr or k <= 0:
        return []

    result = []  # To store the maximums
    dq = deque()  # Deque to store indices

    for i in range(len(arr)):


        # Step 1: Remove indices that are out of the current window
        if dq and dq[0] < i - k + 1:
            print("fff", i)
            dq.popleft()

        # Step 2: Remove indices of elements smaller than the current element
        while dq and arr[dq[-1]] < arr[i]:
            print("d", i)
            dq.pop()

        # Step 3: Add the current index to the deque
        dq.append(i)

        # Step 4: Add the maximum for the current window to the result
        if i >= k - 1:  # Only after the first full window is formed
            result.append(arr[dq[0]])
        print(dq)
    return result

nums = [1,2,3]
# 1, 2
# 2, 3
k = 2
window_maximum_deque(nums, k)
