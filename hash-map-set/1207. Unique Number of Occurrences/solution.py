from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = dict()

        for n in arr:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        return len(d) == len(set(d.values()))
