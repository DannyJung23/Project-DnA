"""
Approach:
Initially, the maximum profit is 0 and the buying price is the first price in the list.
While iterating through the list, update the buying price if a price is lower than the current buying price.
If not, calculate the difference between prices[i] and the current buying price. Update the maximum profit if it's larger than the current maximum profit.
"""

# 65ms solution - O(n)

def maxProfit(self, prices):
    buying_index = 0
    max_profit = 0

    for i in range(buying_index + 1, len(prices)):
        if prices[i] < prices[buying_index]:
            buying_index = i
        else:
            if prices[i] - prices[buying_index] > max_profit:
                max_profit = prices[i] - prices[buying_index]
    
    return max_profit
