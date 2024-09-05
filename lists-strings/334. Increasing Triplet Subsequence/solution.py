from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # first, second = float('inf'), float('inf')

        # for n in nums:
        #     if n <= first:
        #         first = n
        #     elif n > first and n <= second:
        #         second = n
        #     elif n > first and n > second:
        #         return True

        # return False

        if len(set(nums)) < 3:
            return False

        second = None
        for i in range(0, len(nums)):
            n = nums[i]
            second = None
            for j in nums[i+1:]:
                if second is None:
                    if j > n:
                        second = j
                else:
                    if j > second:
                        return True
                    elif j > n:
                        second = j
        return False
