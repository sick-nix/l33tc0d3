from solution import Solution

o = Solution()

assert o.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert o.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
