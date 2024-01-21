def longest_substring_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = ""
    max_result = ""
    for i in range(len(s)):
        if s[i] not in vowels:
            result += s[i]
            if len(result) > len(max_result):
                max_result = result
        else:
            result = ''
    return len(max_result)


s = "codeforintelligents"
print(longest_substring_vowels(s))
