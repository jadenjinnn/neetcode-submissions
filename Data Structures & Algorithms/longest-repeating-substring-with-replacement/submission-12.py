class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        curMax = 0
        sol = 0
        l, r = 0, 0

        while r<len(s):
            freq[s[r]] += 1

            curMax = max(curMax, freq[s[r]])

            while (r-l+1)-curMax > k:
                freq[s[l]] -= 1
                l+=1

            sol = max(sol, r-l+1)
            r+=1

        return sol
