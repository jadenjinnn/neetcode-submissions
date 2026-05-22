class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            mid = (l+r)//2

            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid

        pivot = l

        # print(pivot)

        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[(mid+pivot)%len(nums)] > target:
                r = mid-1
            elif nums[(mid+pivot)%len(nums)] < target:
                l = mid+1
            else:
                return (mid+pivot)%len(nums)

        return -1