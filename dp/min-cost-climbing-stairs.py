def min_cost_climbing_stairs(cost):
    n = len(cost)
    print(n)
    # Initialize an array to store the minimum cost to reach each step
    dp = [0] * (n + 1)
    print(dp)
    
    # Base cases: no cost to start from step 0 or step 1
    dp[0] = 0
    dp[1] = 0
    for i in range(2, n + 1):
        # print(i, min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])) 
        dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
    return dp[n]

cost = [10, 15, 20]

min_cost_climbing_stairs(cost)