import pygame 
from settings import Settings 
from function import  add_blocks, check_events,update_screen,update_bullets
from tank import Tank 
from pygame.sprite import Group 
from block import Block 
def run_game():
    pygame.init()
    settings=Settings()
    
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height))
    pygame.display.set_caption('Tank Fight')
    tanks=Group()
    bullets1=Group()
    bullets2=Group()
    bullets3=Group()
    bullets4=Group()
    blocks=Group()
    tank1=Tank(settings,screen,1)
    tank2=Tank(settings,screen,2)
    tanks.add(tank1)
    tanks.add(tank2)
    add_blocks(settings,screen,blocks)
    

    
    
    while True: 
        
        tank1.update()
        tank2.update()
        check_events(settings,screen,tank1,tank2,bullets1,bullets2,bullets3,bullets4)
        update_bullets(settings,screen,tanks,bullets1,bullets2,bullets3,bullets4,blocks)
        update_screen(settings,screen,tanks,bullets1,bullets2,bullets3,bullets4,blocks)
        
run_game()
