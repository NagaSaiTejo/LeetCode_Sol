class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        for _ in range(k):
            prev_val = grid[m-1][n-1]
            for r in range(m):
                for c in range(n):
                    temp = grid[r][c]
                    grid[r][c] = prev_val
                    prev_val = temp
        return grid