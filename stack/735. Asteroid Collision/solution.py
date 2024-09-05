from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0

        while i < len(asteroids):
            a = asteroids[i]

            if len(stack) > 0:
                last = stack[-1]
                if last > 0 and a < 0:
                    abs_last = abs(last)
                    abs_a = abs(a)
                    if abs_last > abs_a:
                        i += 1
                    elif abs_last < abs_a:
                        stack.pop()
                    else:
                        stack.pop()
                        i += 1
                else:
                    stack.append(a)
                    i += 1
            else:
                stack.append(a)
                i += 1

        return stack
