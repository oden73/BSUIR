from settings import *


class LoadingMenu:
    def __init__(self):
        self.main_surface = pygame.surface.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.main_surface.fill('black')

        self.font = pygame.font.Font("fonts/emulogic.ttf", 50)

        self.text = self.font.render('WORLD 1-1', False, (255, 255, 255))

    def update(self, game):
        game.display_surface.blit(self.main_surface, (0, 0))
        game.display_surface.blit(self.text, (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
