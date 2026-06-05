class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        l, r = 0, 0

        while r<len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1

            seen.add(s[r])
            r+=1
            print(seen, r, l)
            best = max(best, r-l)

        return best