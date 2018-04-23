import pygame
pygame.init()
from random import randint
pygame.font.init()
white =(255,255,255)
black=(0,0,0)
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
        pygame.draw.rect(screen,black,[self._x,self._y,10,10])
    def moveup(self):
        self._y=self._y+self._yspeed
    def movedown(self):
        self._y=self._y-self._yspeed
    def moveright(self):
        self._x=self._x+self._xspeed
    def moveleft(self):
        self._x=self._x-self._xspeed
        
        
class Food:
    def __init__(self,foodx,foody):
        self._x=foodx
        self._y=foody
    def drawfood(self):
        pygame.draw.rect(screen,black,[self._x,self._y,10,10])
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
                if event.key==pygame.K_DOWN:
                    player.movedown()
                if event.key==pygame.K_UP:
                    player.moveup()
        screen.fill(white) 
        player.drawsnake()
        food.drawfood()      
        #Updates the display     
        pygame.display.update()
main()