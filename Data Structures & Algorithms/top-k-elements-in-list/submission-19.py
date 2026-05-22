class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)

        for num in nums:
            freqs[num] += 1

        buckets = [[] for i in range(len(nums))]


        for num, freq in freqs.items():
            buckets[freq-1].append(num)
    
        res = []

        print(buckets)

        for i in range(len(buckets)-1, -1, -1):
            print(i)
            for num in buckets[i]:
                res.append(num)

            if len(res) == k:
                return res
        