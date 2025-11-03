from collections import defaultdict
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        h = defaultdict(int)
        ans = []
        for num in nums:
            for element in num:
                h[element] += 1
        for key in h:
            if h[key] == len(nums):
                ans.append(key)
        ans.sort()
        return ans
        