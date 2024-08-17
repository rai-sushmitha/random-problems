#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lo, hi = prices[0], prices[0]
        res = 0

        for i in range(1,len(prices)):
            if prices[i] < hi:
                res += (hi - lo)
                lo, hi = prices[i], prices[i]
            else:
                hi = max(hi, prices[i])
        return res+(hi-lo)
