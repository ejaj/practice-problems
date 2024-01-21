def find_anagrams(s, p):
    target = [0] * 26
    count = [0] * 26
    start = 0
    result = []
    for c in p:
        target[ord(c) - ord('a')] += 1
    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        if i - start == len(p):
            count[ord(s[start]) - ord('a')] -= 1
            start += 1
        if count == target:
            result.append(start)
    return result

s = "cbaebabacd"
p = "abc"

print(find_anagrams(s, p))
