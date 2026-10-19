import pygame
from sys import exit
from config import *

pygame.init()

def example():

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("HI!")
    clock = pygame.time.Clock() #creates a clock object to control the frame rate

    player=pygame.Rect(150,150,50,50) #creates a rectangle object to represent the player

    def draw():
        window.fill("black") #fills the window with black color
        pygame.draw.rect(window,"red",player) #draws the player rectangle on the window

    while True: #game loop
        for event in pygame.event.get(): #while loop to check for events
            if event.type == pygame.QUIT: #user clicks the X button
                pygame.quit() #removes window
                exit() #terminates the program
        
        keys = pygame.key.get_pressed() #gets the state of all keyboard buttons
        if keys[pygame.K_UP] or keys[pygame.K_w]: #checks if the UP arrow key or W key is pressed
           player.y -= 10 #moves the player rectangle up by 10 pixels 
        if keys[pygame.K_DOWN] or keys[pygame.K_s]: #checks if the DOWN arrow key or S key is pressed
            player.y += 10 #moves the player rectangle down by 10 pixels
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: #checks if the LEFT arrow key or A key is pressed
            player.x -= 10 #moves the player rectangle left by 10 pixels
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: #checks if the RIGHT arrow key or D key is pressed
            player.x += 10 #moves the player rectangle right by 10 pixels

        draw() #calls the draw function to update the display
        pygame.display.update() #updates the display to show changes
        clock.tick(80) #limits the frame rate to 80 frames per second
#example()

