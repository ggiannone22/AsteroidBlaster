import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    pygame.init()                                                             # initializing pygame
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))           # creates new instance of the GUI window
    clock = pygame.time.Clock()                                               # Creating new Clock object
    dt = 0.0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)                          # Adds player to middle of screen
    while True:                                                               # needs infinite loop for gameloop
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                     # Will kill program if user exits out of window
                return  
        screen.fill("black")                                                  # fills the window with black screen
        player.draw(screen)                                                   # draw the player for every loop
        pygame.display.flip()                                                 # Refresh the screen. Has to be always at the end of the loop
        dt = clock.tick(60) / 1000                                            # calculating delta time for fps
        


if __name__ == "__main__":
    main()
