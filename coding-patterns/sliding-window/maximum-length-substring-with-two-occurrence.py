"""
Maximum Length Substring With Two Occurrences
Given a string s, return the maximum length of a  substring such that it contains at most two occurrences of each character.


Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".


Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
"""
from collections import defaultdict


def maximum_length_substring_default_dict(s: str) -> int:
    n = len(s)
    count = defaultdict(int)
    start = 0
    end = 0
    max_length = 0

    while end < n:
        next_char = s[end]
        count[next_char] += 1
        print(count)

        while count[next_char] == 3:
            count[s[start]] -= 1
            start += 1

        max_length = max(max_length, end - start + 1)
        end += 1

    print(max_length)


def maximum_length_substring(s: str) -> int:
    n = len(s)
    count = {}
    start = 0
    end = 0
    max_length = 0

    while end < n:

        # print(end)
        next_char = s[end]
        # print("next", next_char)
        count[next_char] = count.get(next_char, 0) + 1
        # print(count)

        #
        while count[next_char] == 3:
            # print("es")
            # print(start)
            # print()
            count[s[start]] -= 1
            start += 1
            # print("ad", count)
        #

        max_length = max(max_length, end - start + 1)
        # print(next_char)
        end += 1
        # print("after end", end)
        # print("mx", max_length)
        # print()
    print("max", max_length)


input_string = "bcbbbcba"
maximum_length_substring_default_dict(input_string)
