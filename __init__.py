import sys, pygame

WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 454, 525
WINDOW_BG_COLOR = 0, 0, 0

if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.fill(WINDOW_BG_COLOR)
        pygame.display.flip()