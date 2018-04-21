import pygame
from random import randint
pygame.init()
pygame.font.init()
#length will be in units,headx and heady will dictate position 
class snake:
    def __init__(self,length,segments,headx,heady):
        self._length=length
        self._headx=headx
        self._heady=heady
    def drawsnake(self):
        pygame.draw.rect(self._width,self._height,self.locx,self.locy)
    def movesnake(self,xspeed,yspeed):
         move_ip()
        
class food:
    def __init__(self,locx,locy,width,height):
        self._locx=locx
        self._locy=locy
        self._width=width
        self._height=height
    #def drawfood()
     #   self.locx=randint(1,screen_width)
      #  self.locy=randint(1,screen_height)
       # pygame.draw.rect(self._width,self._height,self.locx,self.locy)

        
def main():
    white=(255,255,255)
    black=(0,0,0)
    screen_width=600
    screen_height=600
    screen=pygame.display.set_mode([screen_width,screen_height])
    pygame.display.set_caption('Snake')
    
    screen.fill(white)
    pygame.display.update()
    done=False
    snakex=300
    snakey=300
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        snake.movesnake(-1,0)
    if key[pygame.K_RIGHT]:
        snake.movesnake(1, 0)
    if key[pygame.K_UP]:
        snake.movesnake(0, 1)
    if key[pygame.K_DOWN]:
        snake.movesnake(0, -1)
    while not done:
        True
        #snake.drawsnake()

        

if __name__ == '__main__':
    main()
    pygame.quit()
   


