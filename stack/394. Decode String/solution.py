from string import digits


class Solution:
    def decodeString(self, s: str) -> str:
        res, _ = self.dec(s)
        return res

    def dec(self, s: str) -> tuple[str, str]:
        stack = []

        i = 0
        count = 1

        while i < len(s) and s[i] != "]":
            c = s[i]
            if c in digits:
                count, new_string = self.get_number(s[i:])
                s = new_string
                i = 1
                decoded, new_string = self.dec(s[i:])
                s = new_string
                i = 0
                stack.append(count * decoded)
                continue
            else:
                stack.append(c)
                i += 1

        return "".join(stack), s[i+1:]

    def get_number(self, s: str) -> tuple[int, str]:
        i = 0
        num = ""

        while s[i] in digits:
            num += s[i]
            i += 1

        return int(num), s[i:]
