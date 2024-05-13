"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.



Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.

"""


def longest_nice_substring(s):
    def is_nice(substring):
        chars = set(substring)
        return all(c.lower() in chars and c.upper() in chars for c in chars)

    n = len(s)
    if n == 0:
        return ""

    for length in range(n, 0, -1):
        for start in range(n - length + 1):
            candidate = s[start:start + length]
            if is_nice(candidate):
                return candidate

    return ""


# Example usage
print(longest_nice_substring("YazaAay"))  # Output: "aAa"
print(longest_nice_substring("Bb"))  # Output: "Bb"
print(longest_nice_substring("c"))  # Output: ""
print(longest_nice_substring("cChH"))
