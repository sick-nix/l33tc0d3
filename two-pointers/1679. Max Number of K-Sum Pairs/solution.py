from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ops = 0

        l = 0
        r = len(nums) - 1

        nums.sort()

        while l < r:
            left = nums[l]
            right = nums[r]

            s = left + right
            if s > k:
                r -= 1
            elif s < k:
                l += 1
            else:
                ops += 1
                l += 1
                r -= 1

        return ops
