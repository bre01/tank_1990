import pygame 
from random import randint 
from pygame.sprite import Sprite 
class Block(Sprite):
    def __init__(self,settings,screen,poy):
        super().__init__()
        self.poy=poy
        self.settings=settings 
        self.screen=screen 
        self.image=pygame.image.load('block.bmp')
        self.rect=self.image.get_rect()
        self.rect.centerx=randint(1,2000)
        self.rect.bottom=self.poy
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        