"""
Problem Statement: Given a string, find the length of the longest substring in it with no more than 'K' distinct characters.
Approach:
Use a hash table to remember the frequency of each character in the current window.
Expand the window by adding characters from the right.

If the number of distinct characters in the hash table exceeds 'K',
shrink the window from the left until you're back to 'K' distinct characters.

Update the length of the longest substring as needed during the process.
"""


def longest_substring_with_k_distinct(input_string, k):
    # Initialize a hash table to store the frequency of each character
    char_frequency = {}
    # Initialize variables to keep track of the window start, and the maximum length found
    window_start, max_length, max_substring_start = 0, 0, 0
    for s in range(len(input_string)):
        # print(window_start)
        right_char = input_string[s]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        while len(char_frequency) > k:

            left_char = input_string[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        # Update the maximum length found
        # max_length = max(max_length, s - window_start + 1)
        # Update the maximum length and start position of the longest substring
        if s - window_start + 1 > max_length:
            max_length = s - window_start + 1
            max_substring_start = window_start
    longest_substring = input_string[max_substring_start:max_substring_start + max_length]
    return longest_substring, max_length


input_string = "araaci"
k = 2
longest_substring, length = longest_substring_with_k_distinct(input_string, k)
print("Longest substring:", longest_substring, "with length:", length)
