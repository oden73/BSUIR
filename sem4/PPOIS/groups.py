from settings import *


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = vector(500, 0)

    def draw(self, target_pos):
        self.offset.x = -(target_pos[0] - WINDOW_WIDTH / 2)
        self.offset.x = min(0., self.offset.x)

        # self.offset.y = -(target_pos[1] - WINDOW_WIDTH / 2)

        for sprite in sorted(self, key=lambda drawing_sprite: drawing_sprite.z):
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image, offset_pos)
