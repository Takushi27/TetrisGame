from config import *


class Game:
    def __init__(self):
       #settings
        self.surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
        self.display_surface = pygame.display.get_surface()


        self.display_surface.fill(GREY31)

    def run(self):
        self.display_surface.blit(self.surface, (PADDING,PADDING))