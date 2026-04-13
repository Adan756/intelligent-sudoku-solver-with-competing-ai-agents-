# gui/start_screen.py
import pygame

def start_screen(screen):
    clock = pygame.time.Clock()
    width, height = screen.get_size()
    
    while True:
        screen.fill((10, 10, 20))
        font = pygame.font.SysFont("Verdana", 80, bold=True)
        title = font.render("SUDOKU AI", True, (0, 200, 255))
        screen.blit(title, (width//2 - title.get_width()//2, height//2 - 50))
        
        font_small = pygame.font.SysFont("Verdana", 25)
        sub = font_small.render("Press ENTER or RIGHT ARROW to Start", True, (150, 150, 150))
        screen.blit(sub, (width//2 - sub.get_width()//2, height//2 + 60))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                # Sirf next jane ka option start screen par
                if event.key == pygame.K_RETURN or event.key == pygame.K_RIGHT:
                    return "NEXT"
        clock.tick(60)