class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # strings of different length are never close
        if len(word1) != len(word2):
            return False

        d1 = dict()
        d2 = dict()

        for c in word1:
            if c not in d1:
                d1[c] = 1
            else:
                d1[c] += 1

        for c in word2:
            if c not in d2:
                d2[c] = 1
            else:
                d2[c] += 1

        # strings cannot be close if the don't contain the same letter pool (op 1)
        if set(d1.keys()) != set(d2.keys()):
            return False

        v1 = list(d1.values())
        v1.sort()

        v2 = list(d2.values())
        v2.sort()

        # strings cannot be close if they don't have the same letter occurrences
        if v1 != v2:
            return False

        return True
