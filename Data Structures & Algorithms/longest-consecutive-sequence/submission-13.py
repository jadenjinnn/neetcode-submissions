class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = []

        for num in nums:
            if not num-1 in nums:
                start.append(num)

        longest = 0

        for num in start:
            length = 1
            n = num

            while n+1 in nums:
                length += 1
                n += 1

            longest = max(longest, length)

        return longest