import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidsfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteorids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteorids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteorid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    TimeClock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        player.draw(screen)
        updateable.update(dt)
        for asteorid in asteorids:
            if player.collision(asteorid):
                print("Game Over!")
                pygame.quit()
            for shot in shots:
                if shot.collision(asteorid):
                    asteorid.split()
                    shot.kill()
        pygame.display.flip()
        tick = TimeClock.tick(60)  # Limit to 60 FPS
        dt = tick / 1000


if __name__ == "__main__":
    main()