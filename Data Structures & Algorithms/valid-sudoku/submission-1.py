class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squeres = defaultdict(set)

        M, N = len(board), len(board[0])

        for row in range(M):
            for col in range(N):
                number = board[row][col]
                if number in [",", "."]:
                    continue

                if number in rows[row] or number in cols[col]:
                    return False
                squere_number = int(row/3)*3 + int(col/3)
                if number in squeres[squere_number]:
                    return False
                
                rows[row].add(number)
                cols[col].add(number)
                squeres[squere_number].add(number)

        return True
