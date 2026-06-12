class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0

        q = deque()
        res = []

        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            q.append(r)

            # print(r, l)

            # print(q)

            while r-l+1>k:
                while l>=q[0]:
                    q.popleft()

                l += 1

            # print(q, l, r)                


            if r+1>=k:
                res.append(nums[q[0]])

            

        return res