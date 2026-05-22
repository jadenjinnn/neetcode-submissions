class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        # 3 4 5 6 1 2
        # 1 2 3 4 5 6
        #  2 -> 0        4 pivot

        while l<r:
            mid = l + (r-l)//2

            if nums[mid]>nums[r]:
                l = mid+1
            else:
                r = mid

        # l is the pivot

        l_2, r_2 = 0, len(nums)-1

        while l_2 <= r_2:
            mid = l_2 + (r_2 - l_2)//2

            

            if nums[(mid+l)%len(nums)] > target:
                r_2 = mid-1
            elif nums[(mid+l)%len(nums)] < target:
                l_2 = mid +1
            else:
                return (mid+l)%len(nums)
        return -1

        