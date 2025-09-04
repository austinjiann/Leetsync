from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = defaultdict(int)
        ans = []
        for i in range (len(nums)):
            h[nums[i]]+=1
        heap = []
        for x in h:
            heap.append((h[x],x))
        heapq.heapify(heap)
        count = len(heap)
        while count>k:
            heappop(heap)
            count -= 1
        for b in range (len(heap)):
            ans.append(heap[b][1])
        return ans
        




        
        