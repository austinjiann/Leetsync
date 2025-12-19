class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(curr, i):
            if (len(curr)) == k:
                ans.append(curr[:])
            
            for j in range (i, n):
                curr.append(j+1)
                backtrack(curr, j+1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans
        