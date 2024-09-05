https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/1379369423/?envType=problem-list-v2&envId=heap-priority-queue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while(len(nums)>k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
