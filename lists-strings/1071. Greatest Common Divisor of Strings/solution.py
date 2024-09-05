class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        flag = ""
        len1 = len(str1)
        len2 = len(str2)

        if str1 == str2:
            return str1

        for i in range(0, len1):
            if i == 0:
                sub = str1[0]
                if sub * len1 == str1 and sub * len2 == str2:
                    flag = sub
            elif len1 % i == 0 and len2 % i == 0:
                sub = str1[0:i]
                if sub * (len1 // i) == str1 and sub * (len2 // i) == str2:
                    flag = sub

            if (i > len1 // 2):
                break

            if (i > len2):
                break

        return flag
