"""
Problem Statement
Given a string, find the length of the longest substring where all characters are the same.

Example
Input: "aabbbcccccddd"
Output: 5 (The longest substring where all characters are the same is "ccccc".)

Explanation
In this problem, we need to find the longest contiguous segment (or window) of the string where the same character repeats. We will use a sliding window to track these segments.

Here’s the step-by-step process:

Initialize Pointers: Start with both pointers, say start and end, at the beginning of the string.
Expand Window: Increment the end pointer to expand the window until the character at end is different from the character at start.
Calculate Window Size: When a difference is found, calculate the size of the current window.
Update Maximum Length: If the current window size is greater than the maximum recorded length, update the maximum.
Slide Window: Move the start pointer to the end pointer's position, and repeat the process until you traverse the entire string.
"""


def longest_identical_substring(s):
    if not s:
        return 0

    start = 0
    maxlen = 0
    while start < len(s):
        end = start

        while end < len(s) - 1 and s[end] == s[end + 1]:
            end += 1

        # current_window = s[start:end + 1]
        # print(current_window)
        # current_window_size = len(current_window)
        current_length = end - start + 1
        maxlen = max(maxlen, current_length)
        start = end + 1
    print(maxlen)


str = "aabbbc"
longest_identical_substring(str)
