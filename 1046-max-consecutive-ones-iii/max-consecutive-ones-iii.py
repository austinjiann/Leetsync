#maximum subarray with k 0's
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = ans = 0
        count0 = 0
        for right in range (len(nums)):
            if nums[right] == 0:
                count0 += 1
            while (count0 > k):
                if nums[left] == 0:
                    count0-=1
                left+=1 
            ans = max(ans, right-left+1)
        return ans

        