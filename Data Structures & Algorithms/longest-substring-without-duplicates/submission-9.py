class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        string = set()

        for i, char in enumerate(s):
            while char in string:
                string.remove(s[l])
                l += 1
                

            string.add(char)
            longest = max(longest, i-l+1)

        return longest