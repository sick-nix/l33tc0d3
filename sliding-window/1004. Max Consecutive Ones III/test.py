from solution import Solution

o = Solution()

assert o.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
assert o.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1,
                     1, 0, 0, 0, 1, 1, 1, 1], 3) == 10
