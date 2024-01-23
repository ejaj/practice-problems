def circular_array_loop_exists(arr):
    def next_index(index):
        return (index + arr[index]) % len(arr)

    for i in range(len(arr)):
        slow, fast = i, i

        # Move one step for slow pointer, and two steps for fast pointer
        while (arr[slow] * arr[next_index(slow)] > 0 and arr[fast] * arr[next_index(fast)] > 0 and
               arr[next_index(fast)] * arr[next_index(next_index(fast))] > 0):
            slow = next_index(slow)
            fast = next_index(next_index(fast))

            # If both pointers meet at the same index, there is a cycle
            if slow == fast:
                # Check for loop with only one element
                if slow == next_index(slow):
                    break
                return True

    return False


# Example Usage
print(circular_array_loop_exists([2, -1, 1, 2, 2]))  # True
print(circular_array_loop_exists([-1, 2]))  # False
