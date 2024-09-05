from solution import Solution

o = Solution()

assert o.increasingTriplet([1, 2, 3, 4, 5]) == True
assert o.increasingTriplet([5, 4, 3, 2, 1]) == False
assert o.increasingTriplet([2, 1, 5, 0, 4, 6]) == True
assert o.increasingTriplet([0, 4, 2, 1, 0, -1, -3]) == False
assert o.increasingTriplet([6, 7, 1, 2]) == False
