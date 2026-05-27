class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq, s_freq = defaultdict(int), defaultdict(int)

        for c in t:
            t_freq[c] += 1

        have, need = 0, len(t_freq)

        l, r = 0, 0
        bestlen, best = float("inf"), [-1, -1]

        while r<len(s):
            if s[r] in t_freq:
                s_freq[s[r]] += 1

                if s_freq[s[r]] == t_freq[s[r]]:
                    have += 1

            while have==need:
                # print(s_freq, s[l: r+1], have)
                if r-l+1 < bestlen:
                    bestlen = r-l+1
                    best = [l, r]

                if s[l] in t_freq:
                    s_freq[s[l]] -= 1

                    if s_freq[s[l]] + 1 == t_freq[s[l]]:
                        have -= 1

                l += 1


            r += 1

        return s[best[0]: best[1]+1]