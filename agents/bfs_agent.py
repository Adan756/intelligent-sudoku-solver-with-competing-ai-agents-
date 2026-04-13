# agents/bfs_agent.py
import time
from collections import deque
from utils.validator import is_valid

class BFSAgent:
    def __init__(self, board):
        self.board = [row[:] for row in board]
        self.steps = []
        self.timeout = False # Yeh batayega ke time up hua ya nahi

    def solve(self):
        start_time = time.time()
        queue = deque([(self.board, [])])
        
        while queue:
            # 15 seconds ka check
            if time.time() - start_time > 15:
                self.timeout = True
                break
                
            curr_board, curr_steps = queue.popleft()
            empty = self.find_empty(curr_board)
            
            if not empty:
                return curr_steps # Solution mil gaya

            r, c = empty
            for num in range(1, 10):
                # Har koshish ko steps mein record karein
                self.steps.append(("try", r, c, num))
                if is_valid(curr_board, r, c, num):
                    new_board = [row[:] for row in curr_board]
                    new_board[r][c] = num
                    new_steps = curr_steps + [("place", r, c, num)]
                    queue.append((new_board, new_steps))
                    self.steps.append(("place", r, c, num))

        return self.steps

    def find_empty(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)
        return None