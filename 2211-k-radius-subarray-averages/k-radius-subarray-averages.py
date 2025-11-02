class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        prefixSum = [nums[0]]
        ans = []
        for i in range (1, len(nums)):
            prefixSum.append(nums[i]+prefixSum[i-1])
        
        for x in range (len(prefixSum)):
            if x - k < 0 or x + k >= len(prefixSum):
                ans.append(-1)
            elif x-k == 0:
                ans.append(prefixSum[x+k]//(k*2+1))
            else:
                ans.append((prefixSum[x+k]-prefixSum[x-k-1])//(k*2+1))
        return ans

        