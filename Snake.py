import pygame
from random import randint
pygame.init()
pygame.font.init()
#length will be in units,status will be boolean alive or dead,headx and heady will dictate position 
class snake:
    def __init__(self,length,status,headx,heady):
        self._length=length
        self._status=status
        self._headx=headx
        self._heady=heady
    def drawsnake(self):
        
    def movesnake(self,xspeed,yspeed):
        
class food:
    def __init__(self,locx,locy,width,height):
        self._locx=locx
        self._locy=locy
        self._width=width
        self._height=height
    def drawfood()
        self.locx=randint(1,screen_width)
        self.locy=randint(1,screen_height)
        pygame.draw.rect(self._width,self._height,self.locx,self.locy)

        
def main():
    screen_width=600
    screen_height=600
    screen=pygame.display.set_mode([screen_width,screen_height])
    snakex=300
    snakey=300
    while True:


        

if __name__ == '__main__':
    main()

   


