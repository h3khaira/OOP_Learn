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
done=False
for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
screen=pygame.display.set_mode((800,600))
screen.fill(white)
pygame.display.set_caption('Snake')
pygame.display.update()
#Defining the player snake
class Snake:
    def __init__(self,headx,heady,segments,xspeed,yspeed):
        self._headx=headx
        self._heady=heady
        self._segments=segments
    def drawsnake(self,headx,heady,pastcoord):
        pygame.draw.rect(screen,black,[headx,heady,10,10])
    def movesnake(self,xspeed,yspeed):

#Defines the food blocks    
        class Food:
            def __init__(self,x,y):
                self._x=x
                self._y=y
            def drawfood(self,x,y):
                pygame.draw.rect(screen,black,[x,y,10,10])
            
def main():
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True   
        #Clean the slate
        screen.fill(white)
        #Key Press Handling
        keys=pygame.key.get_pressed()
        if keys[K_LEFT]:
            Snake.movesnake(-1,0)
        if keys[K_RIGHT]:
            Snake.movesnake(1,0)
        if keys[K_UP]:
            Snake.movesnake(0,1)
        if keys[K_DOWN]:
            Snake.movesnake(0,-1)
        #Updates the display     
        pygame.display.update()
