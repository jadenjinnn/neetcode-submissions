class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0

        cur_str = set()

        for r in range(len(s)):
            while s[r] in cur_str:
                cur_str.remove(s[l])
                l += 1
            
            cur_str.add(s[r])
            best = max(best, len(cur_str))

            print(cur_str, best)

        return best