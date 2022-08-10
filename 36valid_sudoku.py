# Runtime: 119 ms, faster than 76.07% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 13.8 MB, less than 99.18% of Python3 online submissions for Valid Sudoku.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        for iterate in range(9):
            check = defaultdict(list)
            for i in range(3):
                for j in range(3):
                    if board[iterate][3*i+j] is not ".":
                        if board[iterate][3*i+j] in check["horizontal"]:
                            # print(f'horizontal / {board[iterate][3*i+j]} / {check["horizontal"]}')
                            return False
                        else:
                            check["horizontal"].append(board[iterate][3*i+j])
                    if board[3*i+j][iterate] is not ".":
                        if board[3*i+j][iterate] in check["vertical"]:
                            # print(f'vertical / {board[3*i+j][iterate]} / {check["vertical"]}')
                            return False
                        else:
                            check["vertical"].append(board[3*i+j][iterate])
                    if board[3*(iterate//3) + i][3*(iterate%3) + j] is not ".":
                        if board[3*(iterate//3) + i][3*(iterate%3) + j] in check["box"]:
                            # print(f'box / {iterate} / {board[3*(iterate//3) + i][3*(iterate%3) + j]} / {check["box"]}')
                            return False
                        else:
                            check["box"].append(board[3*(iterate//3) + i][3*(iterate%3) + j])
        return True