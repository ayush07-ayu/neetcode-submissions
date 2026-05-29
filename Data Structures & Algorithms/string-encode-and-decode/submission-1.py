from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word

        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):

            j = i

            # 1. number (length) read karo
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            # 2. '#' ke baad move karo
            i = j + 1

            # 3. actual word slice karo
            word = s[i:i + length]
            res.append(word)

            # 4. next word pe move
            i = i + length

        return res