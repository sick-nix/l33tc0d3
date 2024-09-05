from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float("-inf")
        s = 0.0

        for i in range(0, len(nums)):
            n = nums[i]
            if i < k - 1:
                s += n
            else:
                s += n
                avg = s / k
                if avg > max_avg:
                    max_avg = avg
                s -= nums[i-k+1]

        return max_avg
