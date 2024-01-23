def sorted_squares(arr):
    n = len(arr)
    result = [0] * n  # Initialize the result array with zeros

    # Initialize two pointers
    left, right = 0, n - 1
    result_index = n - 1  # Start from the end of the result array

    # Traverse the array
    while left <= right:
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2

        if left_square < right_square:
            result[result_index] = right_square
            right -= 1
        else:
            result[result_index] = left_square
            left += 1
        result_index -= 1
    return result


arr = [-4, -1, 0, 3, 10]
print("Sorted Squares: ", sorted_squares(arr))
