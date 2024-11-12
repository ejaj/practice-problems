"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""

def longest_substring_with_replacements(s, k):
    left = 0
    window = {}
    max_length = 0
    max_freq = 0
    
    for right in range(len(s)):
        if s[right] in window:
            window[s[right]] += 1
        else:
            window[s[right]] = 1 
        max_freq = max(max_freq, window[s[right]])
        
        # Check if more than k replacements are needed to make all characters the same
        if (right - left + 1) - max_freq > k:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                 del window[s[left]]
            left += 1
        max_length = max(max_length, right - left + 1) 
    return max_length

s = "AABABBA"
k = 1
print(longest_substring_with_replacements(s, k))  # Output: 4