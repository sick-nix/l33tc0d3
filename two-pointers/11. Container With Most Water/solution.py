from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0

        l = 0
        r = len(height) - 1

        while l < r:
            left = height[l]
            right = height[r]

            x = r - l
            y = min(left, right)

            area = x*y
            if area > 0 and area > max_area:
                max_area = area

            if right < left:
                r -= 1
            else:
                l += 1

        return int(max_area)
