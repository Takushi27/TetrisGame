from config import *
from sys import *

from game import Game
from score import Score
from view import View

class Main:
    def __init__(self):

        #settings
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')



        #components
        self.game = Game()
        self.score = Score()
        self.view = View()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


            #display
            self.display_surface.fill(GRAY)

            #components
            self.game.run()
            self.score.run()
            self.view.run()

            #game update
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    main = Main()
    main.run()