class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for i in range(9):
            uni = set()
            numbers = []

            for j in range(9):
                if board[i][j] in "123456789":
                    rows[i].append(board[i][j])
                    squares[(i//3, j//3)].append(board[i][j])
                    cols[j].append(board[i][j])

        print(cols)


        for row in rows.values():
            if len(set(row)) < len(row):
                return False

        for col in cols.values():
            if len(set(col)) < len(col):
                return False

        for square in squares.values():
            if len(set(square)) < len(square):
                return False


        return True
