class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []

        for i, num in enumerate(nums):
            if num > 0:
                break

            if not i==0 and nums[i-1] == num:
                continue

            l, r = i+1, len(nums)-1

            while l<r:
                if nums[l]+nums[r]+num > 0:
                    r -= 1
                elif nums[l]+nums[r]+num < 0:
                    l += 1
                else:
                    sol.append([nums[i], nums[l], nums[r]])
                    
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1

        return sol