# gui/grid_ui.py
import pygame

# Font ko loop se bahar ek hi baar initialize karein
pygame.font.init()
CELL_FONT = pygame.font.SysFont("Consolas", 35)

def draw_grid(screen, board, cell_size, offset_x=0, offset_y=0):
    for r in range(9):
        for c in range(9):
            x = offset_x + c * cell_size
            y = offset_y + r * cell_size
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (60, 60, 80), rect, 1) 
            
            if board[r][c] != 0:
                # Purana wala font load hata kar global CELL_FONT use karein
                text = CELL_FONT.render(str(board[r][c]), True, (255, 255, 255))
                screen.blit(text, (x + 14, y + 8))