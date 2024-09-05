from solution import Solution

o = Solution()

l = [0, 1, 0, 3, 12]
o.moveZeroes(l)
assert l == [1, 3, 12, 0, 0]

l = [0]
o.moveZeroes(l)
assert l == [0]
