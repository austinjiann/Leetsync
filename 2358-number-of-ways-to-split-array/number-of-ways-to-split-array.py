class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixSum = [nums[0]]
        ans = 0
        for i in range (1, len(nums)):
            prefixSum.append(prefixSum[i-1] + nums[i]) 
        for x in range (len(prefixSum)-1):
            if prefixSum[x] >= prefixSum[-1] - prefixSum[x]:
                ans+=1
        return ans

        