class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_needed = 0
        moves = 0
        for ch in s:
            if ch == '(':
                open_needed += 1
            else: 
                if open_needed > 0:
                    open_needed -= 1
                else:
                    moves += 1
        return moves + open_needed