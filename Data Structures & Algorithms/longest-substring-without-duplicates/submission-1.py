class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        main = 0

        for i in range(len(s)):

            temp = ""

            for j in range(i, len(s)):

                if s[j] not in temp:

                    temp += s[j]

                    if len(temp) > main:
                        main = len(temp)

                else:
                    break

        return main