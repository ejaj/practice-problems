def min_steps(n):
    if n == 1:
        return 0
    dp = [0] * (n + 1)
    for i in range(2, n+1):
        dp[i] = i
        for j in (1, i):
            if i % j == 0:  
                dp[i] = min(dp[i], dp[j] + (i // j))  

    
    print(dp[n])

min_steps(3)