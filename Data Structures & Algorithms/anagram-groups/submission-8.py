from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            freq = [0]*27

            
            for char in string:
                freq[ord(char)-97] += 1
        

            anagrams[tuple(freq)].append(string)

        return list(anagrams.values())