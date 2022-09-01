import pygame
from pygame.sprite import Sprite
class Tank(Sprite):
    def __init__(self,settings,screen,position):
        super().__init__()
        self.settings=settings 
        self.screen =screen 
        self.direction=1 
        self.position=position
        self.image = pygame.image.load( 'tank.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect=self.screen.get_rect()
        self.rect.centerx=self.screen_rect.centerx
        if position ==1:
            self.rect.bottom =self.screen_rect.bottom
        if position ==2:
            self.rect.top=self.screen_rect.top
        self.moving_right=False 
        self.moving_left=False 
        self.moving_up=False 
        self.moving_down=False 

    def update(self):
        if self.moving_down or self.moving_up:
            if self.moving_down:
                self.rect.centery += self.settings.moving_speed
            elif self.moving_up:
                self.rect.centery -= self.settings.moving_speed
        else:
            if self.moving_left:
                self.rect.centerx -= self.settings.moving_speed
            elif self.moving_right:
                self.rect.centerx += self.settings.moving_speed
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)

        

