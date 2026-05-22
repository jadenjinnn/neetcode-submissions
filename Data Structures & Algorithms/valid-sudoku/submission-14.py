class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for y in range(len(board)):
            for x in range(len(board)):
                if board[y][x] in cols[y] or board[y][x] in rows[x] or board[y][x] in squares[(x//3, y//3)]:
                    return False
                elif not board[y][x] == ".":
                    cols[y].add(board[y][x])
                    rows[x].add(board[y][x])
                    squares[(x//3,y//3)].add(board[y][x])

        return True