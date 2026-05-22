class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            prefix = 1
            for j in range(0, i):
                prefix *= nums[j]

            res.append(prefix)

        
        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                res[i] *= nums[j]

        return res

        