import pygame, sys, time
from settings import *

class Game:
    
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((PANE_HEIGHT, PANE_WIDTH))
        pygame.display.set_caption("Zebtari Breakout")
        
        self.background = self.background()
    
    def background(self):
        image = pygame.image.load('/Users/zlakey/breakoutclone/breakoutclone/visual/backgroundpossible.jpg').convert()
        return image
    
    def run(self):
        ttime = time.time()
        while True:
            
            timeChange = time.time() - ttime
            ttime = time.time()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.display_surface.blit(self.background,(0,0))
            
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()