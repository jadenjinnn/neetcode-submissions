class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        mostFreq = 0
        sol = 0


        l = 0

        for r, char in enumerate(s):
            freq[char] += 1
            mostFreq = max(mostFreq, freq[char])

            while (r-l+1)-mostFreq > k:
                freq[s[l]] -= 1
                l += 1

            sol = max(sol, (r-l+1))

        return sol

        