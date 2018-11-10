import sys, pygame

from scripts.controller.GameManager     import GameManager
from scripts.controller.InputManager    import InputManager
from scripts.controller.SceneManager    import SceneManager

WINDOW_BG_COLOR = 0, 0, 0

if __name__ == "__main__":
    pygame.init()
    GameManager.init()

    screen = pygame.display.set_mode(GameManager.get_screen_size())

    # Loop principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       sys.exit()
            elif event.type == pygame.KEYDOWN:  InputManager.key_down(event.key)
            elif event.type == pygame.KEYUP:    InputManager.key_up(event.key)

        screen.fill(WINDOW_BG_COLOR)
        SceneManager.render(screen)
        pygame.display.flip()