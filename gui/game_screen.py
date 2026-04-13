# gui/game_screen.py

import pygame
import time
import threading
from copy import deepcopy
from gui.grid_ui import draw_grid
from gui.start_screen import start_screen
from gui.versus_screen import versus_screen
from gui.difficulty_screen import difficulty_screen
from agents.dfs_agent import DFSAgent
from agents.bfs_agent import BFSAgent
from utils.api import get_sudoku

def run_game():
    pygame.init()
    info = pygame.display.Info()
    screen = pygame.display.set_mode((info.current_w, info.current_h))
    width, height = info.current_w, info.current_h

    # Assets
    robot_left_img = pygame.image.load("assets/tanatos_left.png").convert_alpha()
    robot_right_img = pygame.image.load("assets/even_right.png").convert_alpha()
    robot_h = 300
    robot_w = int(robot_h * (1024 / 1536))
    robot_left = pygame.transform.scale(robot_left_img, (robot_w, robot_h))
    robot_right = pygame.transform.scale(robot_right_img, (robot_w, robot_h))

    current_state = "START"
    selected_difficulty = "easy"
    SUDOKU = None
    ai_status = {"done": False, "dfs_steps": [], "bfs_steps": [], "dfs_time": 0, "bfs_time": 0}

    def solve_background(board_to_solve):
        d_agent = DFSAgent(deepcopy(board_to_solve))
        b_agent = BFSAgent(deepcopy(board_to_solve))
        
        s1 = time.time()
        ai_status["dfs_steps"] = d_agent.solve()
        ai_status["dfs_time"] = time.time() - s1
        
        s2 = time.time()
        ai_status["bfs_steps"] = b_agent.solve()
        ai_status["bfs_time"] = time.time() - s2
        ai_status["done"] = True

    while True:
        if current_state == "START":
            if start_screen(screen) == "NEXT":
                current_state = "DIFFICULTY"

        elif current_state == "DIFFICULTY":
            diff = difficulty_screen(screen)
            if diff == "BACK": current_state = "START"
            else:
                selected_difficulty = diff
                screen.fill((15, 15, 25))
                font = pygame.font.SysFont("Arial", 40, bold=True)
                txt = font.render(f"Fetching {selected_difficulty.upper()} Board...", True, (0, 200, 255))
                screen.blit(txt, (width//2 - txt.get_width()//2, height//2))
                pygame.display.update()
                SUDOKU = get_sudoku(selected_difficulty)
                current_state = "VERSUS"

        elif current_state == "VERSUS":
            sig = versus_screen(screen)
            if sig == "NEXT":
                ai_status["done"] = False
                threading.Thread(target=solve_background, args=(SUDOKU,)).start()
                current_state = "AI_WAIT"
            elif sig == "BACK":
                current_state = "DIFFICULTY"

        elif current_state == "AI_WAIT":
            screen.fill((15, 15, 25))
            font = pygame.font.SysFont("Arial", 40, bold=True)
            txt = font.render("Robots are calculating...", True, (255, 200, 0))
            screen.blit(txt, (width//2 - txt.get_width()//2, height//2))
            pygame.display.update()
            pygame.event.pump() 

            if ai_status["done"]:
                dfs_board = deepcopy(SUDOKU)
                bfs_board = deepcopy(SUDOKU)
                dfs_steps = ai_status["dfs_steps"]
                bfs_steps = ai_status["bfs_steps"]
                dfs_time = ai_status["dfs_time"]
                bfs_time = ai_status["bfs_time"]
                WINNER = "DFS" if dfs_time < bfs_time else "BFS"
                dfs_index, bfs_index = 0, 0
                ANIMATION_SPEED = 10
                start_anim_time = time.time()
                current_state = "GAME"
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); exit()

        elif current_state == "GAME":
            grid_size = 450
            dfs_x = width//4 - grid_size//2.8
            bfs_x = 3*width//4 - grid_size//1.7
            grid_y = height//2 - grid_size//2
            clock = pygame.time.Clock()

            screen.fill((20, 20, 25))

            # Auto-Skip Logic (10 Seconds)
            if time.time() - start_anim_time > 10:
                dfs_index = len(dfs_steps)
                bfs_index = len(bfs_steps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT: current_state = "VERSUS"
                    if event.key == pygame.K_RETURN:
                        dfs_index = len(dfs_steps)
                        bfs_index = len(bfs_steps)

            # DFS Animation
            for _ in range(ANIMATION_SPEED):
                if dfs_index < len(dfs_steps):
                    action = dfs_steps[dfs_index]
                    if action[0] == "place": dfs_board[action[1]][action[2]] = action[3]
                    elif action[0] == "remove": dfs_board[action[1]][action[2]] = 0
                    dfs_index += 1

            # BFS Animation (Try/Place)
            for _ in range(ANIMATION_SPEED):
                if bfs_index < len(bfs_steps):
                    action, r, c, val = bfs_steps[bfs_index]
                    if action == "place":
                        bfs_board[r][c] = val
                    elif action == "try":
                        bfs_board[r][c] = val
                    bfs_index += 1

            # Final Solve Sync
            if dfs_index >= len(dfs_steps):
                for step in dfs_steps:
                    if step[0] == "place": dfs_board[step[1]][step[2]] = step[3]
            if bfs_index >= len(bfs_steps):
                for step in bfs_steps:
                    if step[0] == "place": bfs_board[step[1]][step[2]] = step[3]

            # Drawing
            draw_grid(screen, dfs_board, 50, offset_x=dfs_x, offset_y=grid_y)
            draw_grid(screen, bfs_board, 50, offset_x=bfs_x, offset_y=grid_y)
            screen.blit(robot_left, (dfs_x - robot_w + 20, grid_y + 75))
            screen.blit(robot_right, (bfs_x + grid_size - 39, grid_y + 75))

            # Titles
            font_title = pygame.font.SysFont("Arial", 30, bold=True)
            screen.blit(font_title.render("DFS AGENT", True, (0, 255, 200)), (dfs_x, grid_y - 40))
            screen.blit(font_title.render("BFS AGENT", True, (255, 100, 0)), (bfs_x, grid_y - 40))
            
            diff_font = pygame.font.SysFont("Arial", 28, bold=True)
            diff_text = diff_font.render(f"Difficulty: {selected_difficulty.upper()}", True, (200, 200, 200))
            screen.blit(diff_text, (width//2 - diff_text.get_width()//2, 30))

            # Results & Winner Label
            both_done = (dfs_index >= len(dfs_steps)) and (bfs_index >= len(bfs_steps))
            if both_done:
                f_res = pygame.font.SysFont("Arial", 30, bold=True)
                # Time labels just below the grids
                screen.blit(f_res.render(f"Time: {dfs_time:.4f}s", True, (0,255,200)), (dfs_x, grid_y + grid_size + 20))
                screen.blit(f_res.render(f"Time: {bfs_time:.4f}s", True, (255,100,0)), (bfs_x, grid_y + grid_size + 20))
                
                # Winner Text - Original Position (Middle-Bottom)
                f_big = pygame.font.SysFont("Arial", 50, bold=True)
                winner_color = (0, 255, 200) if WINNER == "DFS" else (255, 100, 0)
                win_txt = f_big.render(f"{WINNER} WINS!", True, winner_color)
                # Positioned slightly above the very bottom
                screen.blit(win_txt, (width//2 - win_txt.get_width()//2, grid_y + grid_size + 80))

            pygame.display.update()
            clock.tick(60)