class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range (len(nums)):
            complement = target - nums[i]
            if complement not in h:
                h[nums[i]] = i
            else:
                return [h[complement], i]
            
        