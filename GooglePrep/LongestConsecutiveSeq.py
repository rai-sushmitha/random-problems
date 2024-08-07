#https://leetcode.com/problems/longest-consecutive-sequence/?envType=company&envId=google&favoriteSlug=google-six-months
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for num in nums:
            if num-1 not in s:
                longest = 1

                while (num+longest) in s:
                    longest = longest + 1
                
                res = max(res, longest)

        return res

        
