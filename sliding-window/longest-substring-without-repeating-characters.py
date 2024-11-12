"""
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

def lengthOfLongestSubstringHashMap(str):
    l = len(str)
    hash_map = {}
    ans = 0
    start = -1
    for i in range(l):
        if str[i] in hash_map and hash_map[str[i]] > start:
            start = hash_map[str[i]]
        hash_map[str[i]] = i
        ans = max(ans, i - start)
    print(ans)

s = "abcabcbb"
lengthOfLongestSubstringHashMap(s)

