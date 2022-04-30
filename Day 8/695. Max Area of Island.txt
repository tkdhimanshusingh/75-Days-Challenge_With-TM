class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited=set()
        def solver(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]==0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            return(1+solver(r-1,c)+solver(r+1,c)+solver(r,c-1)+solver(r,c+1))
        ans=float('-inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited:
                    ans=max(ans,solver(i,j))
        return ans