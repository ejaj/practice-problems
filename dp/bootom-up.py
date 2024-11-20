def coin_change_bottom_up(coins, target):
    # Create an array to store the number of ways to make each amount
    ways = [0] * (target + 1)
    
    # There is 1 way to make 0 (using no coins)
    ways[0] = 1

    # Process each coin
    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

coins = [1, 2, 3]
target = 5
result = coin_change_bottom_up(coins, target)
print(f"Number of ways to make {target} with coins {coins}: {result}")
