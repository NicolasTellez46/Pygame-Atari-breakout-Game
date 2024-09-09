#Nicolas Tellez nrt56
#Purpose: This program uses several other files and objects to create an atari breakout esque game

#Import necessary files for game to function
import pygame
from ball import *
from paddle import *
from text import *
from block import *
import sys


pygame.init()
surface = pygame.display.set_mode((800, 600))

#Colors
red = (255,0,0)
orange = (255,165,0)
yellow = (255,216,0)
green = (0,255,0)
blue = (0,191,255)
purple = (160,32,240)
pink=(255,0,255)

#Instantiated Objects
myBall=Ball(x= 400,y= 400,radius =10,color = pink)
myPaddle = Paddle(200,25, purple)

#TEXT
myScoreBoard = Text("Score: 0",10,10)
winningText = Text("YOUR SCORE WAS ABOVE 100! YOU WIN!",125,350)
pausedText = Text("PAUSED",350,350)
losingText = Text("YOUR SCORE WAS BELOW 100! YOU LOSE!",125,350)

#Ground
ground = Block(x=0,y=585,width=800,height=15,color=(255,255,255))

#blocks
r1 = Block(x=0,y=40,width=200,height=50,color=red)
r2 = Block(x=201,y=40,width=150,height=50,color=red)
r3 = Block(x=352,y=40,width=50,height=50,color=red)
r4 = Block(x=403,y=40,width=150,height=50,color=red)
r5 = Block(x=554,y=40,width=200,height=50,color=red)
r6 = Block(x=755,y=40,width=150,height=50,color=red)

o1 = Block(x=0,y=91,width=150,height=50,color=orange)
o2 = Block(x=151,y=91,width=50,height=50,color=orange)
o3 = Block(x=202,y=91,width=150,height=50,color=orange)
o4 = Block(x=353,y=91,width=200,height=50,color=orange)
o5 = Block(x=554,y=91,width=50,height=50,color=orange)
o6 = Block(x=605,y=91,width=200,height=50,color=orange)

y1 = Block(x=0,y=142,width=50,height=50,color=yellow)
y2 = Block(x=51,y=142,width=200,height=50,color=yellow)
y3 = Block(x=252,y=142,width=50,height=50,color=yellow)
y4 = Block(x=303,y=142,width=150,height=50,color=yellow)
y5 = Block(x=454,y=142,width=200,height=50,color=yellow)
y6 = Block(x=655,y=142,width=150,height=50,color=yellow)

g1 = Block(x=0,y=193,width=150,height=50,color=green)
g2 = Block(x=151,y=193,width=50,height=50,color=green)
g3 = Block(x=202,y=193,width=200,height=50,color=green)
g4 = Block(x=403,y=193,width=150,height=50,color=green)
g5 = Block(x=554,y=193,width=200,height=50,color=green)
g6 = Block(x=755,y=193,width=50,height=50,color=green)

b1 = Block(x=0,y=244,width=50,height=50,color=blue)
b2 = Block(x=51,y=244,width=200,height=50,color=blue)
b3 = Block(x=252,y=244,width=150,height=50,color=blue)
b4 = Block(x=403,y=244,width=50,height=50,color=blue)
b5 = Block(x=454,y=244,width=200,height=50,color=blue)
b6 = Block(x=655,y=244,width=150,height=50,color=blue)

#Adding objects to list
blocks =[]

blocks.append(r1)
blocks.append(r2)
blocks.append(r3)
blocks.append(r4)
blocks.append(r5)
blocks.append(r6)

blocks.append(o1)
blocks.append(o2)
blocks.append(o3)
blocks.append(o4)
blocks.append(o5)
blocks.append(o6)

blocks.append(y1)
blocks.append(y2)
blocks.append(y3)
blocks.append(y4)
blocks.append(y5)
blocks.append(y6)

blocks.append(g1)
blocks.append(g2)
blocks.append(g3)
blocks.append(g4)
blocks.append(g5)
blocks.append(g6)

blocks.append(b1)
blocks.append(b2)
blocks.append(b3)
blocks.append(b4)
blocks.append(b5)
blocks.append(b6)

#Setting values
score = 0
myBall.setXSpeed(5)
myBall.setYSpeed(5)
running = True
fpsClock = pygame.time.Clock()
pause = True
lost = False
collided = False


while running:
     
     #Draws objects to surface
     surface.fill((0, 0, 0))
     pygame.draw.rect(surface, (123,123,123), myBall.get_rect())
     myPaddle.draw(surface)
     myBall.draw(surface)
     myScoreBoard.draw(surface)
     ground.draw(surface)
     
     #Keep looping until there aren't any more blocks 
     if len(blocks) > 0:
         
         if pause:
                pausedText.draw(surface)
                for block in blocks:
                    block.draw(surface)
                    myBall.draw(surface)
         else:
             
             #Move ball
             myBall.move()
             #If the ball intersects the paddle, flipY direction
             if myBall.intersects(myPaddle):
                if collided:
                    collided = False
                    
                else:
                    myBall.setYSpeed(myBall.getYSpeed()*-1)
                    collided = True
                                   
                
                
            
             #Each time the ball touches the ground, player loses 30 points, and flip Y direction
             if myBall.intersects(ground):
                myBall.setYSpeed(myBall.getYSpeed()*-1)
                score-=15
                myScoreBoard.setMessage(f"Score: {score:.0f}")
                        
             for block in blocks:
                 block.draw(surface)
                 #If myBall touches the block, flip Y direction
                 if myBall.intersects(block):
                    myBall.setYSpeed(myBall.getYSpeed()*-1.03)
                    score+=10
                    myScoreBoard.setMessage(f"Score: {score:.0f}")
                    blocks.remove(block)
                    
     #If the player ends the game with more than 150 points, they win, otherwise they lose
     elif score>100:
          winningText.draw(surface)
     else:
          losingText.draw(surface)     
     #Buttons to exit and pause game
     for event in pygame.event.get():
         if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            running = False
         elif event.type == pygame.MOUSEBUTTONDOWN: # Testing
            myBall.setVisible(not myBall.isVisible()) # Testing
        
         if event.type == pygame.KEYDOWN and (event.__dict__['key'] == pygame.K_SPACE):
            if pause == False:
                pause = True
            else:
                pause = False
     pygame.display.update()
     fpsClock.tick(30)
exit() 

