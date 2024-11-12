"""
Longest Substring with at Most K Distinct Characters
input = "abcba" 
k = 2 
output = "bcb."
"""

def longest_substring_k_distinct(s, k):
    left, right = 0, 0
    window = {}
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in window:
            window[s[right]] +=1
        else:
            window[s[right]] = 1
        while len(window) > k:
            window[s[left]] -=1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        
        # max_length = max(max_length, right - left + 1)
        # Update max_length and max_substring if a longer substring is found
        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_substring = s[left:right + 1]
             
    print(max_length, max_substring)        
            
    #$ print(window)
    # print(len(window))
    # print("ddd", max_length)
    

s = "abcba"
k = 2

longest_substring_k_distinct(s, k)