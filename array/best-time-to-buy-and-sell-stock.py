def maxProfit(prices):
    total_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]
    return total_profit


prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
