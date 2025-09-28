class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        search = []
        for i in range (len(matrix)):
            search += matrix[i]
        
        left = 0
        right = len(search)-1
        found = False
        while left <= right:
            middle = (right+left)//2
            if search[middle] == target:
                found = True
                break
            elif search[middle] > target:
                right = middle-1
            else:
                left = middle + 1
        return found
        