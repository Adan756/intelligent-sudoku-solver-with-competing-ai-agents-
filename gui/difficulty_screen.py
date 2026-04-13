# gui/difficulty_screen.py

import pygame

OPTIONS = ["easy", "medium", "hard", "random"]

def difficulty_screen(screen):
    clock = pygame.time.Clock()
    width, height = screen.get_size()

    selected = 0

    while True:
        screen.fill((15, 15, 25))

        title_font = pygame.font.SysFont("Arial", 60, bold=True)
        option_font = pygame.font.SysFont("Arial", 40)

        title = title_font.render("Select Difficulty", True, (0, 200, 255))
        screen.blit(title, (width//2 - title.get_width()//2, 100))

        for i, opt in enumerate(OPTIONS):
            color = (255, 200, 0) if i == selected else (200, 200, 200)
            text = option_font.render(opt.upper(), True, color)
            screen.blit(text, (width//2 - text.get_width()//2, 250 + i*70))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(OPTIONS)
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(OPTIONS)

                if event.key == pygame.K_RETURN:
                    return OPTIONS[selected]

                if event.key == pygame.K_LEFT:
                    return "BACK"

        clock.tick(60)