class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = 0
        curMax = 0
        res=0
        for r in range(len(s)):
            freq[s[r]] += 1
            curMax = max(curMax, freq[s[r]])

            while (r-l+1) - curMax > k:
                freq[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
            r+=1

        return res