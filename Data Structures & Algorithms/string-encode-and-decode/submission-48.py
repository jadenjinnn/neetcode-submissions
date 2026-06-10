class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s

        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            n = ""

            while s[i] != "#":
                n += s[i]
                i += 1

            n = int(n)

            t = ""

            res.append(s[i+1:i+n+1])
            i = i+n+1

        return res