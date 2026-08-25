import pygame
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()                                                             # initializing pygame
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))           # creates new instance of the GUI window
    clock = pygame.time.Clock()                                               # Creating new Clock object
    dt = 0.0
    updatable = pygame.sprite.Group()                                         # Updateable, drawable, and asterodis are all groups
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)                            # Adding Shot instances to shots, updatable, and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable)                    # Adding Asteroid intances to asteroids, updatable, and drawable groups
    AsteroidField.containers = (updatable,)                                   # Adding AsteroidField instances to the updateable group
    Player.containers = (updatable, drawable)                                 # Adding Player instances into drawable and updateable groups
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)                          # Adds player to middle of screen
    asteroid_field = AsteroidField()                          
    while True:                                                               # needs infinite loop for gameloop
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                     # Will kill program if user exits out of window
                return  
            
        screen.fill("black")                                                  # fills the window with black screen

        for n in drawable:
            n.draw(screen)                                                    # draws each drawable instance individually per loop for every frame

        updatable.update(dt)                                                  # updates all updatable instances every loop

        for asteroid in asteroids:
            for shot in shots:                                                # Checking for every shot if it collided with an asteroid, if so split asteroid and kill shot
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()

            if asteroid.collides_with(player) == True:                        # Checks for asteroids collision with player
                log_event("player_hit")
                print("Game Over!") 
                sys.exit()    

        pygame.display.flip()                                                 # Refresh the screen. Has to be always at the end of the loop
        dt = clock.tick(60) / 1000                                            # calculating delta time for fps
        


if __name__ == "__main__":
    main()
