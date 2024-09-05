from solution import Solution

o = Solution()

assert o.closeStrings("abc", "bca") == True
assert o.closeStrings("a", "aa") == False
assert o.closeStrings("cabbba", "abbccc") == True
