import pygame
pygame.init()
from random import randint
pygame.font.init()
white =(255,255,255)
black=(0,0,0)
swidth=800
sheight=600
screen=pygame.display.set_mode((swidth,sheight))
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
        self._xlist=[self._x]
        self._ylist=[self._y]
    def drawsnake(self):
        #pygame.draw.rect(screen,black,[self._x,self._y,10,10])
        for j in range(0,self._length,1):
            pygame.draw.rect(screen,black,[self._xlist[j],self._ylist[j],10,10])
    def update(self): 
        if self._length>1:
            for i in range (self._length,0,-1):
                self._xlist[i-1]=self._xlist[i-2]
                self._ylist[i-1]=self._ylist[i-2]
        self._xlist[0]=self._x
        self._ylist[0]=self._y
    def running(self):
        self._x=self._x+self._xspeed
        self._y=self._y+self._yspeed
    def moveup(self):
        if (self._yspeed != 0.5):
            self._yspeed=-0.5
            self._xspeed=0
    def movedown(self):
        if (self._yspeed != -0.5):
            self._yspeed=0.5
            self._xspeed=0
    def moveright(self):
        if (self._xspeed != -0.5):
            self._xspeed=0.5
            self._yspeed=0
    def moveleft(self):
        if (self._xspeed != 0.5):
            self._xspeed=-0.5
            self._yspeed=0
    def snakeycoord(self):
        return (self._y)
    def snakexcoord(self):
        return (self._x)
    def increasesize(self):
        self._length=self._length+1 
        self._xlist.insert(0,self._x)
        self._ylist.insert(0,self._y)  
    def selfcollision(self):
        for k in range(3,self._length,1):#make it so the head cant collide with the 2nd or 3rd block to avoid issues with overlapping
            if (self._x>=self._xlist[k]+2 and self._x<=self._xlist[k]+8):
                if (self._y>=self._ylist[k]+2 and self._y<=self._ylist[k]+8):
                    return True
    def wallcollision(self):
        if (self._x<=0 or self._x+10>=swidth):
            return True
        if (self._y<=0 or self._y+10>=sheight):
            return True
class Food:
    def __init__(self,foodx,foody):
        self._x=foodx
        self._y=foody
    def drawfood(self):
        pygame.draw.rect(screen,(255,0,0),[self._x,self._y,10,10])
    def respawn(self):
        self._x=randint(1,790)
        self._y=randint(1,590)
    def foodycoord(self):
        return (self._y)
    def foodxcoord(self):
        return (self._x) 
def endscreen():
    screen.fill(black)
    endgame = pygame.font.SysFont('Calibri', 30)
    endgamescreen = endgame.render('Press C to countinue or P to quit', False, (255, 255,255))
    screen.blit(endgamescreen,(175,300))
    restart =True
    while restart:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_c:
                    pygame.display.update()
                    main()
                    restart=False
                if event.key==pygame.K_p:
                    pygame.display.update()
                    pygame.quit()

def main():
    updatecount=0
    player=Snake(300,300,0.5,0,1)#creating player object
    food=Food(100,100) #creating food object
    done=False
    while not done:
        for event in pygame.event.get():#key press handling
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
        player.running()
        #####collision detection with food####
        if ((player.snakexcoord()>=food.foodxcoord() and player.snakexcoord()<=food.foodxcoord()+10)or(player.snakexcoord()+10>food.foodxcoord() and player.snakexcoord()+10<food.foodxcoord()+10)):
            if ((player.snakeycoord()>=food.foodycoord() and player.snakeycoord()<=food.foodycoord()+10)or (player.snakeycoord()+10>food.foodycoord() and player.snakeycoord()+10<food.foodycoord()+10)):
                player.increasesize()
                food.respawn()
                food.drawfood()
        screen.fill(white)
        if updatecount==20:#x,y speed is 0.5, so the snake traverses 10 pixels in 20 iterations, we cant to update every 10 pixels
            player.update()
            updatecount=0
        if player.selfcollision() or player.wallcollision():#quits the game if collision detected
            endscreen()
        updatecount=updatecount+1
        player.drawsnake()
        food.drawfood()      
        #Updates the display     
        pygame.display.update()
main()