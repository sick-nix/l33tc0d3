class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        char_indexes = []
        i = 0

        s_pointer = 0

        while i < len(t) + 1:
            if s_pointer == len(s):
                return True
            if i == len(t):
                if len(char_indexes) > 0:
                    i = char_indexes.pop(0)
                    s_pointer = 0
                    continue
                else:
                    break

            if t[i] == s[s_pointer]:
                s_pointer += 1
            elif s_pointer > 0 and t[i] == s[0]:
                char_indexes.append(i)
            i += 1

        return False
