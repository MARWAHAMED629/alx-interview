#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create an array to store the minimum number of coins
    m_coins = [float('inf')] * (total + 1)
    m_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            # Update the minimum number of coins required for each value
            m_coins[i] = min(m_coins[i], m_coins[i - coin] + 1)

    # Return the minimum number of coins required to reach the total value
    return m_coins[total] if m_coins[total] != float('inf') else -1