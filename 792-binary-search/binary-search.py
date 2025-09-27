class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
        found = False
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                found = True
                return mid
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        if not found: 
            return -1