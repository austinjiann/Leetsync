class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []
        for i in range (len(points)):
            heap.append(((sqrt((points[i][0])**2 + (points[i][1])**2)), [points[i][0], points[i][1]]))
        heapq.heapify(heap)
        for i in range (k):
            ans.append(heap[0][1])
            heappop(heap)
        return ans
        