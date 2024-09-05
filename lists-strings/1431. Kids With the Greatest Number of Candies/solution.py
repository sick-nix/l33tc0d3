from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        m = max(candies)
        for i in candies:
            res.append(i + extraCandies >= m)
        return res
