class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string

        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        j=i
        while i<len(s):
            if s[j] != "#":
                j+=1
            else:
                print(i,j)
                length = int(s[i:j])
                i = j+1
                j = i+length
                res.append(s[i:j])
                i=j
                print(i,j)

        return res