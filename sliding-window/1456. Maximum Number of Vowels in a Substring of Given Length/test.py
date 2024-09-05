from solution import Solution

o = Solution()

assert o.maxVowels("abciiidef", 3) == 3
assert o.maxVowels("aeiou", 2) == 2
assert o.maxVowels("leetcode", 3) == 2
