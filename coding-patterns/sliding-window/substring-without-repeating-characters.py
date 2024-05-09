"""
Problem Statement
Given a string, find the length of the longest substring without repeating characters.

Example
Input: "abcabcbb"
Output: 3 (The longest substring without repeating characters is "abc".)

Explanation
The goal is to find the longest segment (or window) in the string where no character repeats. We use two pointers (or indices) to represent the window's beginning and end, expanding and contracting this window as needed to ensure no character repeats within it.

Here’s how you can solve it step-by-step:

Initialization: Start with both pointers at the beginning of the string. Use a set to track characters within the window.
Expand Right Pointer: Move the right pointer one step at a time, adding characters to the set.
Check for Repeats: If a character is repeated (i.e., already in the set):
Move the left pointer to the right until the repeated character is removed from the window (and thus from the set).
Update Maximum Length: Continuously update the maximum length of the window where no repeats occur.
Repeat: Continue until the right pointer reaches the end of the string.
"""


def length_of_longest_substring(str):
    left = 0
    max_length = 0
    char_set = set()
    for right in range(len(str)):
        while str[right] in char_set:
            char_set.remove(str[right])
            left += 1
        char_set.add(str[right])
        max_length = max(max_length, right - left + 1)
    print(max_length)


if __name__ == '__main__':
    length_of_longest_substring("abcabcbb")
