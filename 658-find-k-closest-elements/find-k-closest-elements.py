from collections import defaultdict
import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        ans = []
        for i in range (len(arr)):
            diff = arr[i]-x
            heapq.heappush(heap,(abs(diff),arr[i]))
        for j in range (k):
            ans.append(heappop(heap)[1])
        ans.sort()
        return ans
        
        