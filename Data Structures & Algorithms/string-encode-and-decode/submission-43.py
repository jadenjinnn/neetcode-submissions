class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        
        for s in strs:
            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i<len(s):
            length = ""

            while not s[i] == "#":
                length += s[i]
                i += 1

            length = int(length)
        
            res.append(s[i+1:i+length+1])

            i= i + length +1

        return res
