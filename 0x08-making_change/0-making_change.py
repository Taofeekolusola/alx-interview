#!/usr/bin/python3
"""
This module contains a function to determine the fewest number of coins needed to meet a given amount total.
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of the values of the coins in your possession.
        total (int): The amount to meet using the fewest number of coins.

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
