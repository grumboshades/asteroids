import pygame, random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        new_velocity_vector_a = self.velocity.rotate(random_angle)
        new_velocity_vector_b = self.velocity.rotate(-random_angle)

        NewAsteroidA= Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        NewAsteroidA.velocity = new_velocity_vector_a * 1.2

        NewAsteroidB = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        NewAsteroidB.velocity = new_velocity_vector_b * 1.2