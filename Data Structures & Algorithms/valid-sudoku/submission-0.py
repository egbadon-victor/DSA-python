class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        r_hash = [[0 for _ in range(n)] for _ in range(n)]
        c_hash = [[0 for _ in range(n)] for _ in range(n)]
        b_hash = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                bh_index = int(f'{i//3}{j//3}',3)
                if element == '.':
                    continue
                element = int(element)
                rh_element = r_hash[i][element-1]
                ch_element = c_hash[j][element-1]
                bh_element = b_hash[bh_index][element-1]

                if rh_element or ch_element or bh_element:
                    return False
                
                r_hash[i][element-1] = element
                c_hash[j][element-1] = element
                b_hash[bh_index][element-1] = element
        return True
