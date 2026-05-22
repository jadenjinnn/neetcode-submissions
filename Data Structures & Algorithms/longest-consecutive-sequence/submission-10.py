class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        sol = 0

        for num in nums:
            if not num-1 in nums:
                length = 1
                n = num

                while n+1 in nums:
                    length+=1
                    n += 1

                sol = max(length, sol)

        return sol