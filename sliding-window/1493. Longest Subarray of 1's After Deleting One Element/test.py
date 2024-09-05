from solution import Solution

o = Solution()

assert o.longestSubarray([1, 1, 0, 1]) == 3
assert o.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
assert o.longestSubarray([1, 1, 1]) == 2
