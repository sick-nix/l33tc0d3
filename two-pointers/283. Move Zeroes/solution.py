from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = 0
        l = len(nums)
        zeroes = 0
        zero_indexes = []

        while i < l and zeroes < l:
            n = nums[i]
            if n == 0:
                zero_indexes.append(i)
            else:
                if len(zero_indexes) > 0:
                    idx = zero_indexes.pop(0)

                    nums[idx] = n
                    nums[i] = 0
                    zero_indexes.append(i)

            i += 1
