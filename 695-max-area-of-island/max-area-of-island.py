class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        def dfs(x,y):
            area = 1
            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                if valid(newX, newY) and (newX, newY) not in seen:
                    seen.add((newX, newY))
                    area += dfs(newX, newY)
            return area
        seen = set()
        directions = [(0,1), (0,-1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        ans = 0
        for i in range (m):
            for x in range (n):
                if grid[i][x] == 1:
                    seen.add((i,x))
                    ans = max(ans, dfs(i,x))
                    
        return ans

