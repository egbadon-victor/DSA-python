class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top= 0
        bot = len(matrix)-1

        while top <= bot:
            row = ((bot - top) // 2) + top
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else: 
                break
        else:
            return False

        target_row = matrix[row]
        l = 0
        r = len(target_row) -1

        while l <= r:
            m = ((r-l)//2) + l

            if target == target_row[m]: return True

            if target < target_row[m]:
                r = m -1
            else:
                l = m+1


        return False
        