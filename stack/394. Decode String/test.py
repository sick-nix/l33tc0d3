from solution import Solution

o = Solution()

assert o.decodeString("3[a]2[bc]") == "aaabcbc"
assert o.decodeString("3[a2[c]]") == "accaccacc"
assert o.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
assert o.decodeString("100[leetcode]") == 100 * "leetcode"
