class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = len(s1)
        freq = [0 for i in range(26)]

        for char in s1:
            freq[ord(char)-ord("a")] += 1

        while r <=len(s2):
            ss = s2[r-len(s1):r]

            # print(ss)
            
            ss_freq = [0 for i in range(26)]

            for char in ss:
                ss_freq[ord(char)-ord("a")] += 1

            if ss_freq == freq:
                return True
            
            r += 1

        return False
