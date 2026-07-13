import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player

def main() -> None:
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    PlayerTriangle = Player(x, y)
    game_clock = pygame.time.Clock()
    dt = 0.0
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        updatable.update(dt)
        for drawable_thing in drawable:
            drawable_thing.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = game_clock.tick(60) / 1000
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
