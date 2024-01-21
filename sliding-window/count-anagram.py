def is_anagram(ana, word):
    s1 = ana.lower()
    s2 = word.lower()
    if sorted(s1) == sorted(s2):
        return True
    return False


def count_anagram(text, word):
    word_len = len(word)
    ana = ''
    count = 0
    d = {}
    for i in range(word_len):
        ana += text[i]
    if is_anagram(ana, word):
        count += 1
    for i in range(1, len(text)):
        ana = ana[1:] + text[i]
        if ana not in d and is_anagram(ana, word):
            count += 1
            d[ana] = 0
        d[ana] = 0
    return count


text = 'gotxxotgxdogt'
word = 'got'
print(count_anagram(text, word))
