# Taylor Olson
# Learning to Program 10E
# 5/4/15

import pygame
pygame.init()

import random 

# Define some colors
BLACK    = (   0,   0,   0)
DARK_GREY = ( 100, 100, 100) # gray 47
GREY = ( 140, 140, 140) # I started with 'gray 63' and mixed it into a new color
LIGHTER_GREY = ( 160, 160, 160) # I started with 'gray 71' and mixed it into a 
#                                 new color
LIGHTEST_GREY = ( 180, 180, 180) # I started with 'gray 90' and mixed it into
#                                  a new circle
POTATOE_WHITE = (168, 137, 91) # I started with 'navajowhite 2' and mixed it
#                                 into a new color
WHITE    = ( 235, 235, 235) #'white*'

LAWN_GREEN = (4, 55, 0) # I started with 'olivedrap 3' and mixed it into 
#                             into a new color
GREEN    = (   0, 135,   0) # 'green*'

RED      = ( 235,   0,   0)
LIGHT_YELLOW   = (130, 130 , 90) # 'lightgoldenrodyellow'

BLUE     = ( 0, 0, 235) #'blue*'
SKY_BLUE = ( 20, 11, 37) #'lightskyblue1'

LIGHT_BROWN = ( 66, 25, 5) # I started with 'goldrenrod' from the website 
#                               and mixed it into a new color
BROWN_SHADOWS = ( 94, 70, 3)# I started with 'darkgoldenrod 4' and mixed it 
#                               into a new color
BROWN    = ( 103, 83, 20) # I started with 'sienna 4' and mixed it into a 
#                            new color
DARK_BROWN = ( 73, 53, 2) #I started with 'sepia' and mixed it into a new color

PI = 3.141592653
 
# Set the height and width of the screen
size = (500, 500)
screen = pygame.display.set_mode(size)

#colors
x_2=255
y_2 = 0

#to time dimming 
dimming = True

#rate in which fireflies move
change_fire_fly_x = 70
change_fire_fly_y = 70

fireflyx = 5
fireflyy = 5

#walking/disapearing footsteps
ball_x1 = 600
ball_y1 = 300
ball_x2 = 600
ball_y2 = 300
foot = 0

#coffee steam

pygame.display.set_caption("My Favorite Constilations")
 
#Loop until the user clicks the close button.
done = False
stars = True
starcounter = 0
clock = pygame.time.Clock()
 
# Loop as long as done == False
while not done:
 
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            
    if stars:
        # Background
        screen.fill(BROWN_SHADOWS)
        
        # Individual wooden boards
        for y_offset in range(20, 700, 100):
            pygame.draw.line(screen, DARK_BROWN, [500, 260 + y_offset], \
                             [0, 360 + y_offset], 2)
                
        # Night sky
        pygame.draw.polygon(screen, SKY_BLUE, [[0, 0], [1750, 0], [0, 360]])
        pygame.draw.polygon(screen, SKY_BLUE, [[500, 0], [500, 288], \
                                               [500/3, 0]])    
        # Table details
            # table texture
        pygame.draw.line(screen, BROWN, [200, 330], [350, 300], 2)
        pygame.draw.line(screen, BROWN, [150, 415], [300, 380], 2)
        pygame.draw.line(screen, BROWN, [230, 505], [470, 455], 2)
            
        # Cup
            # cup body
        for i in range (100): # to create a cylider
            i += 1
            pygame.draw.ellipse(screen,GREY,[105, 305 + i, 105, 55])
            
            # cup top
        pygame.draw.ellipse(screen, LIGHTER_GREY, [105, 305, 105, 55])
        pygame.draw.ellipse(screen, DARK_GREY, [110, 310, 95, 45])  
            
                # cup handle
        pygame.draw.arc(screen, LIGHTER_GREY, [168, 345, 80, 70], 3*PI/2,\
                            5*PI/2, 15) 
        pygame.draw.arc(screen, GREY, [168, 345, 80, 70], 3*PI/2, 5*PI/2, 10)
            
                # cup shine
        for i in range (90): #a fourth of a cylinder
            i += 1
            pygame.draw.arc(screen, LIGHTEST_GREY, [105, 303 + i, 105, 60], \
                            5*PI/3, 11*PI/6)
        
        # for non-special stars in the sky
        for i in range (30):
            y = random.randrange(0,256)
            x = random.randrange(0, 501)
            pygame.draw.ellipse(screen, WHITE, [x,y,1,1])
    
        x = random.randrange(1, 4) #to show more than one pattern
            
        if x == 3: # The Orion Constilation
            pygame.draw.ellipse(screen, WHITE, [70,25,5,5]) #individual stars
            pygame.draw.ellipse(screen, WHITE, [100,20,5,5])
            pygame.draw.ellipse(screen, WHITE, [65,70,5,5])
            pygame.draw.ellipse(screen, WHITE, [83,75,5,5])
            pygame.draw.ellipse(screen, WHITE, [82,105,5,5])
            pygame.draw.ellipse(screen, WHITE, [92,115,10,10])
            pygame.draw.ellipse(screen, WHITE, [120,210,15,15]) #orions belt
            pygame.draw.ellipse(screen, WHITE, [110,290,10,10])
            pygame.draw.ellipse(screen, WHITE, [133,200,15,15])#orions belt
            pygame.draw.ellipse(screen, WHITE, [146,190,15,15])#orions belt
            pygame.draw.ellipse(screen, WHITE, [165,210,10,10])
            pygame.draw.ellipse(screen, WHITE, [180,255,10,10])
            pygame.draw.ellipse(screen, WHITE, [165,130,5,5])
            pygame.draw.ellipse(screen, WHITE, [185,120,10,10])
            pygame.draw.ellipse(screen, WHITE, [300,110,5,5])
            pygame.draw.ellipse(screen, WHITE, [285,80,5,5])
            pygame.draw.ellipse(screen, WHITE, [297,140,5,5])
            pygame.draw.ellipse(screen, WHITE, [240,30,5,5])
            pygame.draw.ellipse(screen, WHITE, [275,200,5,5])
             
            font = pygame.font.SysFont('Calibri', 25, True, False) # to see name
            text = font.render("Orion", True, WHITE)
            screen.blit(text, [430, 10])
            
        elif x == 2: #Leo Constilation
            pygame.draw.ellipse(screen, WHITE, [25, 198, 10, 10])
            pygame.draw.ellipse(screen, WHITE, [120, 197, 5, 5])
            pygame.draw.ellipse(screen, WHITE, [325, 230, 15, 15])
            pygame.draw.ellipse(screen, WHITE, [123, 133, 10, 10])
            pygame.draw.ellipse(screen, WHITE, [330, 170, 5, 5])
            pygame.draw.ellipse(screen, WHITE, [275, 120, 10, 10])
            pygame.draw.ellipse(screen, WHITE, [285, 75, 5, 5])
            pygame.draw.ellipse(screen, WHITE, [355, 40, 5, 5])
            pygame.draw.ellipse(screen, WHITE, [380, 60, 10, 10])
            
            font = pygame.font.SysFont('Calibri', 25, True, False) # to see name
            text = font.render("Leo", True, WHITE)
            screen.blit(text, [440, 15])
            
        else: #big dipper
            pygame.draw.ellipse(screen, WHITE, [70, 90, 15, 15]) 
            pygame.draw.ellipse(screen, WHITE, [120, 80, 15, 15])
            pygame.draw.ellipse(screen, WHITE, [170, 130, 15, 15])
            pygame.draw.ellipse(screen, WHITE, [240, 160, 5, 5])
            pygame.draw.ellipse(screen, WHITE, [260, 210, 10, 10])
            pygame.draw.ellipse(screen, WHITE, [350, 210, 10, 10])
            pygame.draw.ellipse(screen, WHITE, [360, 150, 15, 15])       
            
            font = pygame.font.SysFont('Calibri', 25, True, False) # to see name
            text = font.render("The Big Dipper", True, WHITE)
            screen.blit(text, [340, 10])

     # To sign my picture 
    font = pygame.font.SysFont('Times New Roman', 12, False, True)
    text = font.render("Taylor Olson", True, WHITE)
    screen.blit(text, [0,0])   
    
    #firefly
    pygame.draw.circle(screen,(x_2, x_2, y_2),(fireflyx,fireflyy),6)     
    
    #one foot print
    pygame.draw.circle(screen,BLACK, (ball_x1, ball_y1), 10)
    ball_x1 -= 20
    ball_y1 += 20
    
    pygame.draw.circle(screen,BLACK, (ball_x1-10, ball_y1+10), 10)
    ball_x1 -= 20
    ball_y1 += 20

    #second foot print
    pygame.draw.circle(screen,BLACK, (ball_x2-35, ball_y2), 10)
    ball_x2 -= 20
    ball_y2 += 20

    pygame.draw.circle(screen,BLACK, (ball_x2-45, ball_y2+10), 10)
    ball_x2 -= 20
    ball_y2 += 20 
        
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
  
    if dimming:       
        if x_2 > 0:    
            x_2 = x_2 - 1
        if x_2 == 0:
            dimming = False
            
            #to animate the firefly while its light is out
            fireflyx += change_fire_fly_x
            fireflyy += change_fire_fly_y
                    
            if fireflyx > 500 or fireflyx < 0:
                change_fire_fly_x = change_fire_fly_x * -1
                        
            if fireflyy > 200 or fireflyy < 0:
                change_fire_fly_y = change_fire_fly_y * -1            

    else:             
        if x_2 < 255:
            x_2 = x_2 + 1
        if x_2 == 255:
            dimming = True
            
    if starcounter == 700:    # bigger means slower star refresh
        stars = True
        starcounter = 0
    else:
        stars = False
        starcounter += 1

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
    
    clock.tick(300)   # bigger number means faster flash
    
pygame.quit()


# Explinations
# Big dipper: the big dipper is one of the most well known constillations
# Orion : I know of orions belt, but I wanted to create the entire constillation
# Leo : I am a leo on the zodiac calender 