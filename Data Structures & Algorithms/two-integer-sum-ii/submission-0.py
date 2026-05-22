class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while not numbers[l] + numbers[r] == target and not l == r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

        return [l+1, r+1]
        