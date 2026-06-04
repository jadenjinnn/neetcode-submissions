class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = 0

        for r, num in enumerate(nums):
            while q and num > nums[q[-1]]:
                q.pop()

            q.append(r)

            # print(q, r)

            if r+1>=k:
                if q and l>q[0]:
                    q.popleft()
                
                l+=1

                # print(q)

                res.append(nums[q[0]])

        return res