class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        count = 0
        vowels = "aeiou"

        for i in range(0, len(s)):
            c = s[i]
            if i < k - 1:
                if c in vowels:
                    count += 1
            else:
                if c in vowels:
                    count += 1
                if count > max_vowels:
                    max_vowels = count

                # end early if a sequence of k vowels was found
                # because you cannot find a sequence of vowels longer than k
                if max_vowels == k:
                    break

                if s[i-k+1] in vowels:
                    count -= 1

        return max_vowels
