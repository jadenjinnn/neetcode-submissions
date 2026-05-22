class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1

        buckets = [[] for i in range(len(nums)+1)]

        for num, freq in freqs.items():
            buckets[freq].append(num)

        print(buckets)

        res = []

        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res

