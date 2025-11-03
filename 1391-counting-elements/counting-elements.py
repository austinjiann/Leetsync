class Solution:
    def countElements(self, arr: List[int]) -> int:
        seen = set()
        ans = 0
        for num in arr:
            seen.add(num)
        for x in arr:
            if x+1 in seen:
                ans+=1

        return ans
        
        