from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        transposed = [[grid[j][i]
                       for j in range(len(grid))] for i in range(len(grid[0]))]

        for r in grid:
            for c in transposed:
                if r == c:
                    count += 1

        return count
