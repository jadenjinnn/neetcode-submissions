class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2

        if len(a) > len(b):
            a, b = b, a 

        total = len(a) + len(b)
        half = total // 2

        l, r = 0, len(a)-1

        while True:
            i = (l+r)//2
            j = half-i-2

            aleft = a[i] if i>=0 else float("-inf")
            aright = a[i+1] if i+1<len(a) else float("inf")
            bleft = b[j] if j>=0 else float("-inf")
            bright = b[j+1] if j+1<len(b) else float("inf")

            #  1 2 3 4 | 5
            #  4 | 5 7
            #  1 2 3 4 4 5 7

            if aleft<=bright and aright>=bleft:
                if total % 2:
                    return min(aright, bright)
                else:
                    return (max(aleft, bleft) + min(aright, bright))/2
            elif aleft > bleft:
                r = i-1
            else:
                l = i+1
            

