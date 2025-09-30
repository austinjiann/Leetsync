class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        ans = 0
        while left<=right:
            middle = (left+right)//2
            if nums[middle] == target:
                ans = middle
                return ans
                break
            elif nums[middle]<target:
                left = middle+1
            else:
                right = middle-1
            
        return left
        