class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        if not nums:
            return 0

        possible_start = {}

        for num in nums:
            if num-1 not in nums:
                possible_start[num] = 1

        for start, count in possible_start.items():
            n = start+1

            while n in nums:
                possible_start[start] += 1
                n+=1


        return max(possible_start.values())


        