#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Create a list to store the minimum coins needed for each amount up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: No coins are needed to make 0 amount
    
    # Iterate over each coin and update the dp table
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # If dp[total] is still float('inf'), it means it's not possible to form the total
    return dp[total] if dp[total] != float('inf') else -1
