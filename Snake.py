import pygame
from random import randint
pygame.init()
pygame.font.init()
white =(255,255)
black=(0,0)
snakex=0
snakey=0
foodx=0
foody=0
screen=pygame.display.set_mode((800,800))
pygame.display.set_caption('Snake')
screen=fill(white)

class Snake:
    def __init__(self,headx,heady,segments):
    
    def drawsnake(headx,heady,pastcoord):
        pygame.draw.rect(screen,black,[headx,heady,10,10])
    def movesnake(xspeed,yspeed):
    
class Food:
    def __init__(self,x,y):

    def drawfood(x,y)
        pygame.draw.rect(screen,black,[x,y,10,10])
def main():
    while not done:
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
        pygame.display.update()
