class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1

        sorted_freq = sorted(freqs.items(), key=lambda item: item[1])

        val = []

        for freq in sorted_freq:
            val.append(freq[0])

        return val[-k::]