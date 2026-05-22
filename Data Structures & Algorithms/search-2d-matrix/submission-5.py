class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l<=r:
            mid = l + (r-l)//2

            if target > matrix[mid][-1]:
                l = mid+1
            elif target < matrix[mid][0]:
                r = mid-1
            else:
                l_2, r_2 = 0, len(matrix[mid])-1

                while l_2<=r_2:
                    mid_2 = l_2 + (r_2-l_2)//2


                    if target > matrix[mid][mid_2]:
                        l_2 = mid_2+1
                    elif target < matrix[mid][mid_2]:
                        r_2 = mid_2-1
                    else:
                        return True

                return False
        return False
        