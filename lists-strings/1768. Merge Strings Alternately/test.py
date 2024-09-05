from solution import Solution

o = Solution()

assert o.mergeAlternately("abc", "pqr") == "apbqcr"
assert o.mergeAlternately("ab", "pqrs") == "apbqrs"
assert o.mergeAlternately("abcd", "pq") == "apbqcd"
