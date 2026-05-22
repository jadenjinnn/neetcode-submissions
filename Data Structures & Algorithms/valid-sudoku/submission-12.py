class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for i in range(9):
            for j in range(9):
                if not board[i][j] == ".":
                    rows[i].append(board[i][j])
                    cols[j].append(board[i][j])
                    squares[(i//3, j//3)].append(board[i][j])

        print(rows, cols, squares)

        for i in range(9):
            if len(set(rows[i])) < len(rows[i]):
                return False

            if len(set(cols[i])) < len(cols[i]):
                return False

        for square in squares.values():
            if len(set(square)) < len(square):
                return False

        return True
