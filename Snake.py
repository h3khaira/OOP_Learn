import pygame
pygame.init()
from random import randint
pygame.font.init()
white =(255,255,255)
black=(0,0,0)
snakex=0
snakey=0
foodx=0
foody=0
screen=pygame.display.set_mode((800,600))
screen.fill(white)
pygame.display.set_caption('Snake')
pygame.display.update()

class Snake:
    def __init__(self,x,y,xspeed,yspeed,length):
        self._x=x
        self._y=y
        self._xspeed=xspeed
        self._yspeed=yspeed
        self._length=length
    def drawsnake(self):
        pygame.draw.rect(screen,black,(10,10))
    def moveup(self):
        self._y=self._y+yspeed
    def movedown(self):
        self._y=self._y-yspeed
    def moveright(self):
        self._x=self._x+xspeed
    def moveleft(self):
        self._x=self._x-xspeed
        
        
class Food:
    def __init__(self,foodx,foody):
        self._x=foodx
        self._y=foody
    def drawfood(self):
        pygame.draw.rect(screen,black,(10,10))
    #def respawn(self):

  
def main():
    player=Snake(300,300,1,0,1)
    food=Food(100,100)
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True 
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    player.moveleft()
                if event.key==pygame.K_RIGHT:
                    player.moveright()
        # #Clean the slate
        # screen.fill(white)       
        # #Updates the display     
        # pygame.display.update()
main()