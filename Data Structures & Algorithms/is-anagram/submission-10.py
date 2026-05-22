from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = defaultdict(int)

        for char in s:
            chars[char] += 1

        for char in t:
            chars[char] -= 1

        for count in chars.values():
            if not count == 0:
                return False

        return True