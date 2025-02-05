from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer1 = list(set(nums1) - set(nums2))
        answer2 = list(set(nums2) - set(nums1))

        answer = [answer1, answer2]
        return answer
