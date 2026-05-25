class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1f = [0 for i in range(26)]
        s2f = [0 for i in range(26)]

        for i in range(len(s1)):
            s1f[ord(s1[i])-ord("a")] += 1
            s2f [ord(s2[i])-ord("a")] += 1

        matches = 0

        for i in range(26):
            if s1f[i] == s2f[i]:
                matches += 1

        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            i = ord(s2[r])-ord("a")

            s2f[i] += 1

            if s2f[i] == s1f[i]:
                matches += 1
            elif s1f[i] + 1 == s2f[i]:
                matches -= 1

            i = ord(s2[l])-ord("a")

            s2f[i] -= 1

            if s2f[i] == s1f[i]:
                matches += 1
            elif s1f[i] - 1 == s2f[i]:
                matches -= 1

            l += 1

        return matches==26