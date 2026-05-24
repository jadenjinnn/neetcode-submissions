class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)-1
        k = 0

        while l<=r:
            while l<=r and nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                k += 1

            l += 1
        
        print(nums)
        return len(nums)-k