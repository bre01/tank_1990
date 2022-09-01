import pygame 
from pygame.sprite import Sprite 

class Bullet(Sprite):

    def __init__(self,settings,screen,tank):
        super().__init__()
        self.screen = screen 
        self.rect=pygame.Rect(0,0,settings.bullet_width,settings.bullet_height)
        self.direction=tank.direction
        if self.direction==1:
            self.rect.centerx=tank.rect.centerx
            self.rect.bottom=tank.rect.top
        elif self.direction==2:
            self.rect.left=tank.rect.right
            self.rect.centery=tank.rect.centery
        elif self.direction==3:
            self.rect.centerx=tank.rect.centerx
            self.rect.top=tank.rect.bottom
        elif self.direction==4:
            self.rect.right=tank.rect.left
            self.rect.centery=tank.rect.centery
        self.color=settings.bullet_color 
        self.bullet_speed=settings.bullet_speed
        self.direction=1
    def update1(self):
        self.rect.centery -=self.bullet_speed
    def update2(self):
        self.rect.centerx +=self.bullet_speed
    def update3(self):
        self.rect.centery +=self.bullet_speed
    def update4(self):
        self.rect.centerx -=self.bullet_speed
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
