# https://leetcode.com/discuss/interview-question/5536572/google-online-assessment-maximum-frequency-subarray
# Input : arr = [1, 2, 1, 3, 4, 2, 4, 3, 3, 4]
# not tested
class Solution:
    def maxSubarrayLength(self, nums: List[int]) -> int:
        numDict = {}

        i, j = 0, 0
        n = len(nums)
        res = 0

        for i in range(len(nums)):
          numDict[nums[i]] = numDict.get(nums[i], 0) + 1
          
        k = min(numDict, k = numDict.get)

        while(j<n):
            numDict[nums[j]] = numDict.get(nums[j], 0) + 1
            while(numDict[nums[j]] > k):
                numDict[nums[i]] -= 1
                i=i+1

            res = max(res, j-i+1)
            j=j+1
        
        return res
