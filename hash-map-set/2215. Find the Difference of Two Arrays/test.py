from solution import Solution

o = Solution()

assert o.findDifference([1, 2, 3], [2, 4, 6]) == [[1, 3], [4, 6]]
assert o.findDifference([1, 2, 3, 3], [1, 1, 2, 2]) == [[3], []]
