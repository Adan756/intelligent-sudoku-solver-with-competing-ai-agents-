# gui/versus_screen.py
import pygame
import random

def versus_screen(screen):
    clock = pygame.time.Clock()
    WIDTH, HEIGHT = screen.get_size()
    
    # Load assets ONCE before loop
    left_img = pygame.image.load("assets/tanatos_left.png").convert_alpha()
    right_img = pygame.image.load("assets/even_right.png").convert_alpha()
    vs_img = pygame.image.load("assets/vs1.png").convert_alpha()

    target_h = int(HEIGHT * 0.9) 
    target_w = int(target_h * (1024 / 1536)) 
    left_robot = pygame.transform.scale(left_img, (target_w, target_h))
    right_robot = pygame.transform.scale(right_img, (target_w, target_h))
    vs_final_size = int(WIDTH * 0.25)
    
    rob_y = HEIGHT - target_h
    lx, rx = -target_w, WIDTH
    target_lx, target_rx = -50, WIDTH - target_w + 50 
    
    vs_scale, vs_alpha = 0.1, 0
    vs_triggered = False

    while True:
        screen.fill((5, 5, 15)) 
        
        if lx < target_lx: lx += (target_lx - lx) * 0.1 + 2
        else: lx = target_lx
        if rx > target_rx: rx -= (rx - target_rx) * 0.1 + 2
        else: rx = target_rx

        if abs(lx - target_lx) < 100: vs_triggered = True

        screen.blit(left_robot, (lx, rob_y))
        screen.blit(right_robot, (rx, rob_y))
        
        if vs_triggered:
            if vs_scale < 1.0: vs_scale += 0.08
            if vs_alpha < 255: vs_alpha += 15
            curr_w, curr_h = int(vs_final_size * vs_scale), int(vs_final_size * vs_scale)
            vs_scaled = pygame.transform.scale(vs_img, (curr_w, curr_h))
            vs_scaled.set_alpha(vs_alpha)
            vs_rect = vs_scaled.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(vs_scaled, vs_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: return "BACK"
                if (event.key == pygame.K_RETURN or event.key == pygame.K_RIGHT) and vs_alpha >= 255:
                    return "NEXT"
        clock.tick(60)