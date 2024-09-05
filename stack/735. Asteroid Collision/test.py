from solution import Solution

o = Solution()

assert o.asteroidCollision([5, 10, -5]) == [5, 10]
assert o.asteroidCollision([8, -8]) == []
assert o.asteroidCollision([10, 2, -5]) == [10]
