def longest_sunstring(s, k):
    high, low, start, end = 0, 0, 0, 0
    windows = set()
    freq = [0] * 128
    while high < len(s):
        windows.add(s[high])
        freq[ord(s[high])] += 1
        while len(windows) > k:
            freq[ord(s[low])] -= 1
            if freq[ord(s[low])] == 0:
                windows.remove(s[low])
            low += 1

        if start - end < high - low:
            end = high
            start = low
        high += 1
    return s[start:end + 1]


s = 'abcb'
k = 2
# Output = 'bdbdbbd'

print(longest_sunstring(s, k))
