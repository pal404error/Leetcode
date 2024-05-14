class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxs = collections.defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                n = board[row][col]
                
                if n!= ".":
                    if n in rows[row] or n in cols[col] or n in boxs[(row // 3, col // 3)] : 
                        return False
                
                rows[row].add(n)
                cols[col].add(n)
                boxs[(row // 3, col//3)].add(n)
        
        return True