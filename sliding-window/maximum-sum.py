import sys
k = 2
arr = [100, 200, 300, 400]
n = len(arr)
# INT_MIN = -sys.maxsize - 1
# max_sum = INT_MIN
# Brute force
# for i in range(n-k+1):
#     current_sum = 0
#     for j in range(k):
#         current_sum = current_sum + arr[i + j]
#     max_sum = max(current_sum, max_sum)
# print(max_sum)

# window_sum = 0
# for i in range(k):
#     window_sum += arr[i]
# print(window_sum)

# sliding window technic
window_sum = sum(arr[:k])
max_sum = window_sum
for i in range(n-k):
    window_sum = window_sum - arr[i] + arr[i+k]
    max_sum = max(window_sum, max_sum)
print(max_sum)


ss = '1, 2.5, e, 7'
ll = list(ss.split(', '))
clean_list = my_list = [eval(s) for s in ll if all(c.isdigit() or c == "." for c in s)]
print(sum(clean_list)//len(clean_list))