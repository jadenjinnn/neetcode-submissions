class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = [0 for i in range(26)]
        s2freq = [0 for i in range(26)]

        for c in s1:
            s1freq[ord(c)-ord("a")] += 1

        l = 0


        have, need = 0, 0

        for i in s1freq:
            if i>0:
                need += 1

        for r in range(len(s2)):
            i = ord(s2[r])-ord('a')

            if s1freq[i]>0:
                s2freq[i] += 1

                if s2freq[i] == s1freq[i]:
                    have += 1
                elif s2freq[i]-1 == s1freq[i]:
                    have -= 1

            if r+1>len(s1):
                j = ord(s2[l])-ord('a')

                if s2freq[j] >0: 
                    s2freq[j] -= 1

                    if s2freq[j]==s1freq[j]:
                        have += 1
                    elif s2freq[j]+1==s1freq[j]:
                        have -= 1

                l+=1

            print(s2freq)

            if have==need:
                return True

        return False