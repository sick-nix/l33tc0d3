from solution import Solution

o = Solution()

assert o.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
assert o.pivotIndex([1, 2, 3]) == -1
assert o.pivotIndex([2, 1, -1]) == 0
