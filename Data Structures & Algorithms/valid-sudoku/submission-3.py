class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                
                val = 1 << (int(board[r][c]) - 1)
                if val & rows[r] or val & cols[c] or val & squares[(r//3)*3 + (c//3)]:
                    return False
                rows[r] |= val
                cols[c] |= val
                squares[(r//3)*3+(c//3)] |= val
        return True