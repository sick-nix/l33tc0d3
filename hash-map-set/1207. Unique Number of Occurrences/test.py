from solution import Solution

o = Solution()

assert o.uniqueOccurrences([1, 2, 2, 1, 1, 3]) == True
assert o.uniqueOccurrences([1, 2]) == False
assert o.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]) == True
