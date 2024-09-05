class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rest = ''
        if len(word1) > len(word2):
            rest = word1[len(word2):]
            word1 = word1[:len(word2)]
        elif len(word2) > len(word1):
            rest = word2[len(word1):]
            word2 = word2[:len(word1)]

        res = ''
        for i in range(0, len(word1)):
            res += word1[i] + word2[i]

        return res + rest
