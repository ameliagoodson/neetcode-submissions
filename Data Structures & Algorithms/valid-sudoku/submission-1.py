class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)  # create defaultdicts with default val of set
        rows = defaultdict(set)
        # object with row number as key as set of seen values as val {0: {"5", "3"}}
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if (
                    (board[row][col] in rows[row])
                    or board[row][col] in cols[col]
                    or board[row][col] in squares[(row // 3, col // 3)]
                ):
                    return False
                cols[col].add(board[row][col])
                rows[row].add(board[row][col])
                squares[(row // 3, col // 3)].add(board[row][col])

        return True
