import pygame
import random
pygame.init()
pygame.font.init()
#length will be in units,status will be boolean alive or dead,headx and heady will dictate position 
class snake:
    def __init__(self,length,status,headx,heady):
        snake.length=length
        snake.status=status
        snake.headx=headx
        snake.heady=heady
    def drawsnake()
        
class food:
    def __init__(self,locx,locy,width,height):
        food.locx=locx
        food.locy=locy
        food.width=width
        food.height=height
    def drawfood()

        
def main():
    screen_width=600
    screen_height=600
    screen=pygame.display.set_mode([screen_width,screen_height])
    while True:
        pass

if __name__ == '__main__':
    main()
   


