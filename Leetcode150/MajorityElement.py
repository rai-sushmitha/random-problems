# This is solved using Moore's Voting Algorithm, refer random-problems/notes/MooreVotingAlgo
# Leetcode: https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = nums[0]

        for i in range(0, len(nums)):
            if count == 0:
                candidate = nums[i]
            
            if nums[i] == candidate:
                count = count+1
            else:
                count = count-1
        return candidate
