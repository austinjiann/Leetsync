class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k
        curr = sum(nums[:right])
        ans = curr/k
        while right < len(nums):
            curr -= nums[left]
            left+=1
            right+=1
            curr += nums[right-1]
            ans = max(ans,curr/k)
        return ans
            

            
        