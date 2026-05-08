class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for i in range(9)]
        cols=[set() for i in range(9)]
        box=[set() for i in range(9)]
        for r in range(9):
            for c in range(9):
                curr_val=board[r][c]
                if curr_val==".":
                    continue
                box_index = (r // 3) * 3 + (c // 3)
                if curr_val in rows[r] or curr_val in cols[c] or curr_val in box[box_index]:
                    return False 
                else:
                    rows[r].add(curr_val)
                    cols[c].add(curr_val)
                    box[box_index].add(curr_val)
        return True
