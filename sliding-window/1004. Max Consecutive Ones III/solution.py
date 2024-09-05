from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ones = 0
        zeroes = []
        l = 0
        r = 0

        while l <= r and r < len(nums):
            n = nums[r]

            if n == 0:
                zeroes.append(r)

            count = r - l + 1
            if len(zeroes) <= k:
                if count > max_ones:
                    max_ones = count
            else:
                if nums[l] == 0:
                    zeroes.pop(0)
                l += 1
            r += 1

        return max_ones
