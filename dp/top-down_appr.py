def coin_change_top_down(coins, target):
    memo = {}
    def helper(remaining):
        # Base cases
        if remaining == 0:
            return 1  # One way to make 0 (using no coins)
        if remaining < 0:
            return 0  # No way to make a negative amount
        
        if remaining in memo:
            return memo[remaining]
         # Recursive case: try every coin
        total_ways = 0
        for coin in coins:
            total_ways += helper(remaining - coin)
        memo[remaining] = total_ways
        return total_ways
    return helper(target)

# Example usage
coins = [1, 2, 3]
target = 5
result = coin_change_top_down(coins, target)
print(f"Number of ways to make {target} with coins {coins}: {result}")
