class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = defaultdict(int)

        for c in t:
            t_freq[c] += 1

        have, need = 0, len(t_freq)

        l, r = 0, 0

        window = defaultdict(int)
        best, bestlen = [-1, -1], float("inf")

        while r<len(s):
            window[s[r]] += 1

            if s[r] in t_freq and window[s[r]] == t_freq[s[r]]:
                have += 1

            # print(window)

            while have == need:
                if (r-l+1) < bestlen:
                    best = [l ,r]
                    bestlen = r-l+1

                window[s[l]] -= 1

                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    have -= 1

                
                l += 1

            r+=1

        return s[best[0]:best[1]+1] if bestlen != float("inf") else ""                