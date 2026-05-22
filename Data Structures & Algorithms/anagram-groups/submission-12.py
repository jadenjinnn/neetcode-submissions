class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            freq = [0 for i in range(26)]

            for char in s:
                freq[ord(char)-ord("a")] += 1

            res[tuple(freq)].append(s)

        return list(res.values())