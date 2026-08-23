import pygame
import constants
from logger import log_state

def main():
    pygame.init()                                                                       # initializing pygame
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print (f"Screen width: {constants.SCREEN_WIDTH}")
    print (f"Screen height: {constants.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)) # creates new instance of the GUI window
    clock = pygame.time.Clock()                                                         # Creating new Clock object
    dt = 0.0

    while True:                                                                         # needs infinite loop for gameloop
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                               # Will kill program if user exits out of window
                return

        screen.fill("black")                                                            # fills the window with black screen
        pygame.display.flip()                                                           # Refresh the screen. Has to be always at the end of the loop
        dt = clock.tick(60) / 1000                                                      # calculating delta time for fps
        


if __name__ == "__main__":
    main()
