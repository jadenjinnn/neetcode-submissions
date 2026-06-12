class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tfreq = defaultdict(int)
        sfreq = defaultdict(int)

        for c in t:
            tfreq[c] += 1

        l, r = 0, 0
        best = [-1, -1]
        bestlen = float("inf")
        have, want = 0, len(tfreq)

        while r<len(s):
            if s[r] in t:
                sfreq[s[r]] += 1

                if sfreq[s[r]] == tfreq[s[r]]:
                    have += 1
            
            while have==want:
                print(s[l:r+1])
                if r-l+1 < bestlen:
                    bestlen = r-l+1
                    best = [l,r]

                if s[l] in t:
                    sfreq[s[l]] -= 1

                    if sfreq[s[l]]+1 == tfreq[s[l]]:
                        have -= 1

                l += 1

            r+=1

        return s[best[0]:best[1]+1]