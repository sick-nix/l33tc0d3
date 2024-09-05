from solution import Solution

o = Solution()

assert o.compress(["a", "a", "b", "b", "c", "c", "c"]) == 6
assert o.compress(["a"]) == 1
assert o.compress(["a", "b", "b", "b", "b", "b", "b",
                  "b", "b", "b", "b", "b", "b"]) == 4
