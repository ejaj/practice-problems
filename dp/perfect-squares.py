import math

def num_squares(n):
    # dp[i] will hold the minimum number of perfect squares that sum up to i
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # 0 squares are needed to make 0
    print("d", dp)
    for i in range(1, n + 1):
        # print(i)
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            print(dp)
            j += 1
    print(dp[n])
num_squares(3)