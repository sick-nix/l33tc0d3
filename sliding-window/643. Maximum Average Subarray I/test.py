from solution import Solution

o = Solution()

assert o.findMaxAverage([1, 12, -5, -6, 50, 3], 4) == 12.75
assert o.findMaxAverage([5], 1) == 5.0
assert o.findMaxAverage([3, 3, 4, 3, 0], 3) == 3.33
