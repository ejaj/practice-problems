def equal_substring(s, t, maxCost):
    n = len(s)
    cost = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
    print(cost)
    start = 0
    total_cost = 0
    max_length = 0
    for end in range(n):
        total_cost += cost[end]
        print(total_cost)
        # If cost exceeds maxCost, reduce window size from the left
        while total_cost > maxCost:
            total_cost -= cost[start]
            start += 1
        max_length = max(max_length, end - start + 1)
    print(max_length)
def equal_substring_al(s, t, maxCost):
    start = 0
    total_cost = 0
    max_length = 0
    for end in range(len(s)):
        total_cost += abs(ord(s[end])-ord(t[end]))
        while total_cost > maxCost:
            total_cost -= abs(ord(s[start]) - ord(t[start]))
            start +=1
        max_length = max(max_length, end - start + 1)
    print(max_length)
    
s = "abcd"
t = "bcdf"
maxCost = 3
equal_substring_al(s, t, maxCost)