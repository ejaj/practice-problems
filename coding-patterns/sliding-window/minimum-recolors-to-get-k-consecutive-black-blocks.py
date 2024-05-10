"""
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.



Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW".
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
Example 2:

Input: blocks = "WBWBBBW", k = 2
Output: 0
Explanation:
No changes need to be made, since 2 consecutive black blocks already exist.
Therefore, we return 0.


Constraints:

n == blocks.length
1 <= n <= 100
blocks[i] is either 'W' or 'B'.
1 <= k <= n
"""


def minimumConsecutiveBlackBlocks(blocks, k):
    n = len(blocks)
    if k > n:
        return -1  # If k is greater than the length of the string, it's impossible to have k consecutive 'B's.

    count_of_whites = sum(1 for i in range(k) if blocks[i] == 'W')
    print(count_of_whites)

    # Initialize the minimum operations to the number of 'W's in the first window
    min_operations = count_of_whites

    # Sliding window to process the rest of the blocks
    for i in range(1, n - k + 1):
        print(blocks[i])
        # If the block that is leaving the window is a 'W', decrease the count
        if blocks[i - 1] == 'W':
            count_of_whites -= 1
        # If the block that is entering the window is a 'W', increase the count
        if blocks[i + k - 1] == 'W':
            count_of_whites += 1

        # Update the minimum operations needed
        min_operations = min(min_operations, count_of_whites)

    return min_operations


# # Example 1
# blocks1 = "WBBWWBBWBW"
# k1 = 7
# print(minimumConsecutiveBlackBlocks(blocks1, k1))  # Expected output: 3

# Example 2
blocks2 = "WBWBBBW"
k2 = 2
print(minimumConsecutiveBlackBlocks(blocks2, k2))  # Expected output: 0
