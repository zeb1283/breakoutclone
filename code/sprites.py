import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((PANE_WIDTH // 15, PANE_HEIGHT // 80))
        
        self.image.fill('white')
        
        self.rect = self.image.get_rect(center = (PANE_WIDTH // 2, PANE_HEIGHT - 50))
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.speed = 300
        
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def block(self):
        if self.rect.left < 10:
            self.rect.left = 10
            self.pos.x = self.rect.x
        if self.rect.right > PANE_WIDTH - 10:
            self.rect.right = PANE_WIDTH - 10
            self.pos.x = self.rect.x
        
    def update(self, timeChange):
        self.input()
        self.pos.x += self.direction.x * self.speed * timeChange
        self.rect.x = round(self.pos.x)