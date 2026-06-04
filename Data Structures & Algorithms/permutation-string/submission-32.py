class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freq = defaultdict(int)

        for c in s1:
            s1freq[c] += 1

        have, need = 0, len(s1freq)

        s2freq = defaultdict(int)

        l, r = 0, 0

        while r<len(s2):
            if s2[r] in s1freq:
                s2freq[s2[r]] += 1

                if s2freq[s2[r]] == s1freq[s2[r]]:
                    have += 1
                elif s2freq[s2[r]]-1 == s1freq[s2[r]]:
                    have -= 1

            if r+1>len(s1):
                if s2[l] in s2freq:
                    s2freq[s2[l]] -= 1

                    if s2freq[s2[l]] == s1freq[s2[l]]:
                        have += 1
                    elif s2freq[s2[l]] + 1== s1freq[s2[l]]:
                        have -= 1
                
                l += 1

            print(s2freq, have, r, l)

            if have == need:
                return True

            r += 1

        return False