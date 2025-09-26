class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        ans = 0
        maxWeight = 5000
        for i in range (len(weight)):
            maxWeight -= weight[i]
            if maxWeight >= 0:
                ans+=1
            else:
                break
        return ans
        