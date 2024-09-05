from typing import List
import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        no_zeroes = [i for i in nums if i != 0]
        zeroes_count = len(nums) - len(no_zeroes)

        if zeroes_count > 1:
            return [0] * len(nums)

        prod = math.prod(no_zeroes)

        for i in nums:
            if zeroes_count == 1:
                if i == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(int(prod * (math.pow(i, -1))))

        return res
