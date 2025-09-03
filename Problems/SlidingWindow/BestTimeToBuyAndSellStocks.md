# Problem: Best time to buy and sell stocks
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy
```
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval = float('inf')
        maxprofit = 0
        
        for i in prices:
            minval = i if i < minval else minval
            if i - minval > maxprofit:
                maxprofit = i - minval
                
        return maxprofit
```