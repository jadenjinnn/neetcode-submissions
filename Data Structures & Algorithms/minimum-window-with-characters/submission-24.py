class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfreq = defaultdict(int)

        for c in t:
            tfreq[c] += 1

        have, need = 0, len(tfreq)

        sfreq = defaultdict(int)

        l, r = 0, 0

        best = [-1, -1]
        bestlen = float("inf")

        while r<len(s):
            if s[r] in tfreq:
                sfreq[s[r]] += 1

                if sfreq[s[r]] == tfreq[s[r]]:
                    have += 1



            while have == need:

                if r-l+1 <bestlen:
                    bestlen = r-l+1
                    best = [l, r]

                if s[l] in sfreq:
                    sfreq[s[l]] -=1

                    if sfreq[s[l]]+1 == tfreq[s[l]]:
                        have -= 1


                

                l += 1
            print(r, l, sfreq, have)

            r += 1

        # while l<=r:



        return s[best[0]:best[1]+1]