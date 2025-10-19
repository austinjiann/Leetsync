class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binarySearch(arr, target):
            left = 0
            right = len(arr)-1
            while left <= right:
                mid = (left+right)//2
                if arr[mid] == target:
                    return mid+1
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
            return left
        nums.sort()
        presum = [nums[0]]
        ans = []
        for i in range (1,len(nums)):
            presum.append(presum[i-1]+nums[i])
        for query in queries:
            ans.append(binarySearch(presum, query))
        print(presum)
        return ans
                

        
            
                

