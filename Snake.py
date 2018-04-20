import pygame
#pygame.init()
pygame.font.init()
#length will be in units,status will be boolean alive or dead,headx and heady will dictate position 
class snake:
    def __init__(self,length,status,headx,heady):
        snake.length=length
        snake.status=status
        snake.headx=headx
        snake.heady=heady
class food:
    def __init__(self,locx,locy):
        food.locx=locx
        food.locy=locy
        
def main():
    screen_width=600
    screen_height=600
    pygame.display.set_mode([screen_width,screen_height])
    pygame.display.flip()
    while True:
        pass



