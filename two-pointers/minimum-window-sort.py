"""
Problem Statement:
Given an unsorted array, find the minimum length of the subarray, which, if sorted, will sort the entire array.

Approach:
Find the Unsorted Subarray:
Identify the first element from the left that is out of order (greater than its next element).
Identify the first element from the right that is out of order (less than its previous element).
Find the Minimum and Maximum Elements:
Find the minimum and maximum values in this subarray.
Expand the Window:
Extend the window's left boundary to include any elements that are greater than the minimum of the subarray.
Extend the window's right boundary to include any elements that are less than the maximum of the subarray.

"""


def minimum_window_sort(arr):
    n = len(arr)
    if n <= 1:
        return 0, 0, 0  # Returning 0 length and dummy window indices

    # Step 1: Find the unsorted subarray
    left, right = 0, n - 1
    while left < n - 1 and arr[left] <= arr[left + 1]:
        left += 1
    if left == n - 1:  # The array is already sorted
        return 0, 0, 0  # Returning 0 length and dummy window indices
    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1

    # Step 2: Find min and max in the subarray
    subarray_min = min(arr[left:right + 1])
    subarray_max = max(arr[left:right + 1])

    # Step 3: Expand the window
    while left > 0 and arr[left - 1] > subarray_min:
        left -= 1
    while right < n - 1 and arr[right + 1] < subarray_max:
        right += 1

    return right - left + 1, left, right


# Example usage
arr = [1, 2, 5, 3, 4, 7, 10, 6, 8, 9]
length, start, end = minimum_window_sort(arr)
print("Length of minimum window to sort: ", length)
print("Window to sort: ", arr[start:end + 1])
