
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile/k)
            return hours <= h
        
        left = 1 #min eating speed
        right = max(piles) #max eating speed
        while left <= right:
            mid = (left+right)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left
        