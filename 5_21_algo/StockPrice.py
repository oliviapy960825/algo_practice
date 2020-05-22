"""

This problem was asked by Facebook.

Given an array of numbers representing the stock prices of a company in 
chronological order and an integer k, return the maximum profit you can 
make from k buys and sells. You must buy the stock before you can sell 
it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should 
return 3.
"""
class Solution(object):
def maxProfit(self, k, prices):
    """
    :type k: int
    :type prices: List[int]
    :rtype: int
    """
    if not k or not prices: return 0
    if k >= len(prices)/2:
        return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
    release=[0]*k
    hold = [float("-inf")]*k
    for price in prices:
        for i in range (k-1, -1, -1):
            release[i] = max(release[i], hold[i]+price)
            if i==0: hold[i] = max(hold[i], -price)
            else: hold[i] = max(hold[i], release[i-1]-price)
    return release[-1]