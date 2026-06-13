class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)

        l = 0

        mostFrequent = 0
        best = 0

        for r, c in enumerate(s):
            freq[c] += 1
            mostFrequent = max(mostFrequent, freq[c])

            while r-l+1-mostFrequent>k:
                freq[s[l]] -= 1
                l += 1

            best = max(best, r-l+1)

        return best