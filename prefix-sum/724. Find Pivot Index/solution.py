from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        pivot = -1

        for i in range(0, len(nums)):
            if left_sum == right_sum - nums[i]:
                pivot = i
                break

            left_sum += nums[i]
            right_sum -= nums[i]

        return pivot
