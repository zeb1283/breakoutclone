import pygame, sys, time
from settings import *
from sprites import Player

class Game:
    
    def __init__(self):
        pygame.init()
        self.displaySurface = pygame.display.set_mode((PANE_WIDTH, PANE_HEIGHT))
        pygame.display.set_caption("Zebtari Breakout")
        self.genSprites = pygame.sprite.Group()
        self.background = self.background()
        self.player = Player(self.genSprites)
    
    def run(self):
        ttime = time.time()
        while True:
            
            timeChange = time.time() - ttime
            ttime = time.time()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            
            self.displaySurface.blit(self.background,(0,0))
            self.genSprites.update(timeChange)
            self.genSprites.draw(self.displaySurface)
            
            pygame.display.update()
    
    def background(self):
        bimage = pygame.image.load('/Users/zlakey/breakoutclone/visual/backgroundpossible.jpg').convert()
        return bimage

if __name__ == '__main__':
    game = Game()
    game.run()