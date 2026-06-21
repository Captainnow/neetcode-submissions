import collections
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # Fixed typo: 'collection' to 'collections'

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                
                # Check for duplicates
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r // 3, c // 3)]):
                    return False # Fixed logical bug: Must return False if invalid
                
                # Add to sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c]) # Fixed indexing bug: 'rows[c]' to 'rows[r]'
                squares[(r // 3, c // 3)].add(board[r][c])
                
        return True
