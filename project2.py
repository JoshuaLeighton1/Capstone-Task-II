import pygame
import random

pygame.init()

#giving the screen a height and width

screen_width = 1040
screen_height = 640

screen = pygame.display.set_mode((screen_width,screen_height)) #this creates the screen

#create the players and enemies

player1 = pygame.image.load("player.jpg")
enemy1 = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("image.png")
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")


#boundary detection

p_height = player1.get_height()
p_width = player1.get_width()
e_height = enemy1.get_height()
e_width = enemy1.get_width()
e2_height = enemy2.get_height()
e2_width = enemy2.get_width()
e3_height = enemy3.get_height()
e3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()


print("This is the height of the player image: " +str(p_height))
print("This is the width of the player image: " +str(p_width))
print("This is the height of the enemy image: " +str(e_height))
print("This is the width of the enemy image: " +str(e_width))
print("This is the height of the monster image:" +str(e2_height))
print("This is the width of the monster image: " +str(e2_width))
print("This is the height of the prize image:" +str(prize_height))
print("This is the width of the prize width:" +str(prize_width))


#store the positions of the players and enemies as variables

player1XPosition = 0
player1YPosition = 10

#enemy starts at a random position

enemy1XPosition = screen_width
enemy1YPosition = random.randint(0, screen_height - e_height)

enemy2XPosition = screen_width
enemy2YPosition = random.randint(0, screen_height - e2_height)

enemy3XPosition = screen_width
enemy3YPosition = random.randint(0, screen_height - e3_height)

#start the priez at a random position

prizeXPosition = random.randint(0, screen_width - prize_width)
prizeYPosition = random.randint(0, screen_height - prize_height)


                                 
#check if any movement keys are pressed

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

#define the game loop

while 1:
    
    screen.fill(0) #clears screen
    screen.blit(player1, (player1XPosition,player1YPosition)) #puts player on screen
    screen.blit(enemy1, (enemy1XPosition,enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition,enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition,enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
  

    pygame.display.flip() # this updates the screen

    #loop through the events of this game

    for event in pygame.event.get():
        #check if the user quits the program

        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        #check if the user presses a key down.

        if event.type == pygame.KEYDOWN:
            #Test if the key pressed is the one we want.

            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True

        #this event checks if the key is up( not pressed by the user)
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
                
        #after the events are checked the players moves accordingly

    if keyUp == True:
        if player1YPosition > 0:
            player1YPosition -= 1
    if keyDown == True:
        if player1YPosition  < screen_height - p_height:
            player1YPosition += 1
    if keyLeft == True:
        if player1XPosition > 0:
            player1XPosition -= 1
    if keyRight == True :
        if player1XPosition < screen_width - p_width :
            player1XPosition += 1

#need to check for collisions with the player
    playerBox = pygame.Rect(player1.get_rect())

    playerBox.top = player1YPosition
    playerBox.left = player1XPosition


#box for the enemy
    enemyBox1 = pygame.Rect(enemy1.get_rect())
    enemyBox1.top = enemy1YPosition
    enemyBox1.left = enemy1XPosition


    enemyBox2 = pygame.Rect(enemy2.get_rect())
    enemyBox2.top = enemy2YPosition
    enemyBox2.left = enemy2XPosition

    enemyBox3 = pygame.Rect(enemy3.get_rect())
    enemyBox3.top = enemy3YPosition
    enemyBox3.left = enemy3XPosition
    
#Box for the prize
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
    
#test the collisions of the boxes

    if playerBox.colliderect(enemyBox1):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemyBox2):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(enemyBox3):
        print("You lose!")
        pygame.quit()
        exit(0)

    if playerBox.colliderect(prizeBox):
        print("You win!")
        pygame.quit()
        exit(0)
#if prize goes off screen you lose
    if prizeXPosition < 0 - prize_width:
        print("You lose!")
        pygame.quit()
        exit(0)

         
    enemy1XPosition -= 0.05
    enemy1YPosition += 0.02
    enemy2XPosition -= 0.02
    enemy2YPosition -= 0.01
    enemy3XPosition -= 0.05
    prizeYPosition +- 0.02
    prizeXPosition -= 0.02



