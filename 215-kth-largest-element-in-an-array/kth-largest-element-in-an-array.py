import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range (len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        for i in range (k):
            kBiggest = heappop(nums)
        return kBiggest*-1
        

        