class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1



        while l<=r:
            mid = (r + l) // 2

            if target > matrix[mid][-1]:
                l = mid+1
            elif target < matrix[mid][0]:
                r = mid-1
            else:
                x = mid
                l, r = 0, len(matrix[x])-1

                while l<=r:
                    mid = (l+r)//2

                    if target>matrix[x][mid]:
                        l = mid+1
                    elif target<matrix[x][mid]:
                        r = mid-1
                    else:
                        return True

                return False
                

        return False