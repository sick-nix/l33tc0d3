from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        current = None
        i = 0
        count = 1

        for j in range(0, len(chars) + 1):
            if j == len(chars):
                c = "AAA"
            else:
                c = chars[j]

            if current is None:
                current = c
                count = 1
            else:
                if current == c:
                    count += 1
                else:
                    chars[i] = current
                    i += 1

                    if count == 1:
                        pass
                    else:
                        if count < 10:
                            chars[i] = str(count)
                            i += 1
                        else:
                            for k in str(count):
                                chars[i] = k
                                i += 1

                    current = c
                    count = 1

        return i
