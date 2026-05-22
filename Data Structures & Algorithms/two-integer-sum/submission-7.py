class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}

        for i, num in enumerate(nums):
            if num in remainder:
                return [remainder[num], i]

            remainder[target-num] = i