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
# #Defining the player snake
class Snake:
    def __init__(self,x,y,,xspeed,yspeed):
        self._x=x
        self._y=y
        self._xspeed=xspeed
        self._yspeed=yspeed
    def move(self):

# #Defines the food blocks  
# 
#   
def main():
    player=Snake(300,300,1,0)
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True 
        # #Clean the slate
        # screen.fill(white)       
        # #Updates the display     
        # pygame.display.update()
main()