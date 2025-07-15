# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit= 0
        min_el = inf
        
        for price in prices:
            if price < min_el:
                min_el = price
                continue
            max_profit = max(max_profit, price - min_el)
        
        return max_profit