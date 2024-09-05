from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flag = False

        i = 0
        count = 0
        while i < len(flowerbed):
            if count == n:
                flag = True
                break

            if flowerbed[i] == 1:
                i += 2
                continue
            else:
                if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    count += 1
                    i += 2
                    continue

            i += 1

        if count == n:
            flag = True
        return flag
