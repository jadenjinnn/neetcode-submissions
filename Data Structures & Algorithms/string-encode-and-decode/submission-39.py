class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for string in strs:
            encoded += str(len(string)) + "#" + string

        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        j = i
        res = []
        while i < len(s):
            print((i,j))
            if s[j] != "#":
                j += 1

            else:
                length = int(s[i:j])
                i=j+1
                j = i +length

                res.append(s[i:j])
                i=j

        return res
