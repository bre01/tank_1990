import pygame 
import sys 
from bullet import Bullet 
from tank import Tank 
from block import Block 
def check_events(settings,screen,tank1,tank2,bullets1,bullets2,bullets3,bullets4):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            check_keydown_events(settings,screen,event,tank1,tank2,bullets1,bullets2,bullets3,bullets4)
        if event.type==pygame.KEYUP:
            check_keyup_events(event,tank1,tank2)
def check_keyup_events(event,tank1,tank2):
    if event.key==pygame.K_a:
        tank1.moving_left=False
    if event.key== pygame.K_d:
        tank1.moving_right=False 
    if event.key== pygame.K_w:
        tank1.moving_up=False 
    if event.key==pygame.K_s:
        tank1.moving_down=False  
    if event.key==pygame.K_LEFT:
        tank2.moving_left=False
    if event.key==pygame.K_RIGHT:
        tank2.moving_right=False 
    if event.key==pygame.K_UP:
        tank2.moving_up=False 
    if event.key==pygame.K_DOWN:
        tank2.moving_down=False 

def update_screen(settings,screen,tanks,bullets1,bullets2,bullets3,bullets4,blocks):
    screen.fill(settings.bg_color)
    for bullet in bullets1:
        bullet.draw_bullet()
    for bullet in bullets2:
        bullet.draw_bullet()
    for bullet in bullets3:
        bullet.draw_bullet()
    for bullet in bullets4:
        bullet.draw_bullet()    
    
    tanks.draw(screen)
    blocks.draw(screen)
    
    pygame.display.flip()

def check_keydown_events(settings,screen,event,tank1,tank2,bullets1,bullets2,bullets3,bullets4):
    if event.key==pygame.K_a:
        tank1.direction=4
        tank1.moving_left=True
    
        
    if event.key==pygame.K_d:
        tank1.direction=2 
        tank1.moving_right=True 
        
    if event.key== pygame.K_w:
        tank1.direction=1
        tank1.moving_up=True  
        
    if event.key==pygame.K_s:
        tank1.direction=3    
        tank1.moving_down=True 
    if event.key==pygame.K_LEFT:
        tank2.moving_left=True
        tank2.direction=4
    if event.key==pygame.K_RIGHT:
        tank2.moving_right=True 
        tank2.direction=2 
    if event.key==pygame.K_UP:
        tank2.moving_up=True 
        tank2.direction=1
    if event.key==pygame.K_DOWN:
        tank2.moving_down=True 
        tank2.direction=3  
    if event.key==pygame.K_SPACE:
        fire_bullets(settings,screen,tank1,bullets1,bullets2,bullets3,bullets4)
    if event.key==pygame.K_l:
        fire_bullets(settings,screen,tank2,bullets1,bullets2,bullets3,bullets4)
def update_bullets(settings,screen,tanks,bullets1,bullets2,bullets3,bullets4,blocks):
    
    for bullet in bullets1.sprites():
        bullet.update1()
        if bullet.rect.centery < 0:
            bullets1.remove(bullet)
    for bullet in bullets2:
        bullet.update2()
        if bullet.rect.centerx >settings.screen_width:
            bullets2.remove(bullet)
    for bullet in bullets3:   
        bullet.update3()
        if bullet.rect.centery >settings.screen_height:
            bullets3.remove(bullet)
    for bullet in bullets4:
        bullet.update4()
        if bullet.rect.centerx <0:
            bullets4.remove(bullet)
    check_bullet_tank_collisions(settings,screen,tanks,bullets1,bullets2,bullets3,bullets4,blocks)


def fire_bullets(settings,screen,tank,bullets1,bullets2,bullets3,bullets4):
    if tank.direction  ==1:
        new_bullet1=Bullet(settings,screen,tank)
        bullets1.add(new_bullet1)
    if tank.direction==2:
        new_bullet2=Bullet(settings,screen,tank)
        bullets2.add(new_bullet2)
    if tank.direction==3:
        new_bullet3=Bullet(settings,screen,tank)
        bullets3.add(new_bullet3)
    if tank.direction==4:
        new_bullet4=Bullet(settings,screen,tank)
        bullets4.add(new_bullet4)
def check_bullet_tank_collisions(settings,screen,tanks,bullets1,bullets2,bullets3,bullets4,blocks):
    collisions=pygame.sprite.groupcollide(bullets1,tanks,True,True)
    collisions=pygame.sprite.groupcollide(bullets2,tanks,True,True)
    collisions=pygame.sprite.groupcollide(bullets3,tanks,True,True)
    collisions=pygame.sprite.groupcollide(bullets4,tanks,True,True)
    collisions=pygame.sprite.groupcollide(bullets1,blocks,True,False)
    collisions=pygame.sprite.groupcollide(bullets2,blocks,True,False)
    collisions=pygame.sprite.groupcollide(bullets3,blocks,True,False)
    collisions=pygame.sprite.groupcollide(bullets4,blocks,True,False)
def add_blocks(settings,screen,blocks):
    for number in range(1,11):
        for number2 in range(1,6):
            new_block=Block(settings,screen,number*100)
            blocks.add(new_block)

