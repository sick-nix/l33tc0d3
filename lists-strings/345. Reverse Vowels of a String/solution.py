class Solution:
    def reverseVowels(self, s: str) -> str:
        res = list(s)
        indexes = [i for i in range(0, len(s)) if s[i].lower() in 'aeiou']

        l = len(indexes)
        for i in range(0, l // 2):
            start_idx = indexes[i]
            end_idx = indexes[l - i - 1]
            tmp = res[start_idx]
            res[start_idx] = res[end_idx]
            res[end_idx] = tmp

        return "".join(res)
