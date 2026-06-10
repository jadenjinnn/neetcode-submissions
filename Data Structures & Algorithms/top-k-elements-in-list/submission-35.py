class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        buckets = [[] for i in range(len(nums))]

        for num, count in freq.items():
            buckets[count-1].append(num)

        print(buckets)

        res = []

        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                # print(num)
                if num in freq:
                    res.append(num)
                    if len(res)==k:
                        return res