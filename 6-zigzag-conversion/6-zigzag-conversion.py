class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [""] * numRows
        
        row_index = 0
        step = 1
        
        for ch in s:
            rows[row_index] += ch
        
            if row_index == 0:
                step = 1
            elif row_index == (numRows - 1):
                step = -1
        
            row_index += step
        
        return "".join(rows)