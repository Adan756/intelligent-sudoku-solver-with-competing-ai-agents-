# agents/dfs_agent.py
from utils.validator import is_valid

class DFSAgent:
    def __init__(self, board):
        self.board = [row[:] for row in board]
        self.steps = []

    def solve(self):
        self._dfs()
        return self.steps

    def _dfs(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:

                    for num in range(1, 10):
                        if is_valid(self.board, row, col, num):

                            self.board[row][col] = num
                            self.steps.append(("place", row, col, num))

                            if self._dfs():
                                return True

                            # Backtrack
                            self.board[row][col] = 0
                            self.steps.append(("remove", row, col, num))

                    return False
        return True
