def is_anagram(ana, word):
    s1 = ana.lower()
    s2 = word.lower()
    if sorted(s1) == sorted(s2):
        return True
    return False


def check_inclusion(s1, s2):
    word_len = len(s1)
    ana = ''
    d = {}
    per = False
    for i in range(word_len):
        ana += s2[i]
    if is_anagram(ana, s1):
        per = True
    for i in range(1, len(s2)):
        ana = ana[1:] + s2[i]
        if ana not in d and is_anagram(ana, s1):
            per = True
            d[ana] = 0
        d[ana] = 0
    return per


s1 = "ab"
s2 = "eidbaooo"
print(check_inclusion(s1, s2))
