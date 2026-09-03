class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=collections.defaultdict(set)
        rows=collections.defaultdict(set)
        squares=collections.defaultdict(set)
        for R in range(9):
            for C in range(9):
                if board[R][C]==".":
                    continue
                if (board[R][C] in rows[R] or
                    board[R][C] in cols[C]or
                    board[R][C] in squares[(R//3,C//3)]):
                    return False
                cols[C].add(board[R][C])    
                rows[R].add(board[R][C])    
                squares[(R//3,C//3)].add(board[R][C])
        return True

            


        