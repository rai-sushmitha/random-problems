#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo = prices[0]
        i = 1
        res = 0

        while(i<len(prices)):
            if (prices[i] < lo):
                lo = prices[i]
            res = max(res, prices[i]-lo)
            i+=1
        return res
