class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
            
        for string in strs:    
            freqs = [0 for i in range(26)]

            for char in string:
                freqs[ord(char)-ord("a")] += 1

            anagrams[tuple(freqs)].append(string)

        return list(anagrams.values()) 