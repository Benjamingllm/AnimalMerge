
import pymunk
import pygame
import math
from .config import ASSETS_DIR
ANIMAL_COLLISION = 1

class Animal:
    size = 0
    points = 0
    image = None
    level = 0
    sprite = None
    def __init__(self, x, y):
        self.time_above_line = 0.0
        self.mass =self.size * 0.01 
        moment = pymunk.moment_for_circle(self.mass, 0, self.size)
        self.body = pymunk.Body(self.mass, moment)
        self.body.position = (x, y)
        
        self.shape = pymunk.Circle(self.body, self.size)
        self.shape.elasticity = 0.5
        self.shape.friction = 1
        self.shape.collision_type = ANIMAL_COLLISION

        if self.image is None and self.sprite is not None:
            self.load_sprite()
        
    @classmethod
    def load_sprite(cls):
        cls.image = pygame.image.load(cls.sprite).convert_alpha()
        rect = cls.image.get_bounding_rect()
        cls.image = cls.image.subsurface(rect)
        cls.image = pygame.transform.smoothscale(cls.image, (cls.size * 2, cls.size * 2))
    
    def draw(self, screen):
        rotated = pygame.transform.rotate(self.image, -math.degrees(self.body.angle))
        rect = rotated.get_rect(center = self.body.position)
        screen.blit(rotated,rect)


class Mouse(Animal):
    size = 14
    points = 1
    sprite = ASSETS_DIR / "mouse.png"


class Hamster(Animal):
    size = 18
    points = 3
    sprite = ASSETS_DIR / "hamster.png"


class Fox(Animal):
    size = 36
    points = 15
    sprite =  ASSETS_DIR /"fox.png"


class Dog(Animal):
    size = 44
    points = 21
    sprite = ASSETS_DIR / "dog.png"


class Sheep(Animal):
    size = 53
    points = 28
    sprite =  ASSETS_DIR / "sheep.png"


class Cow(Animal):
    size = 63
    points = 36
    sprite = ASSETS_DIR /"cow.png"

class Dragon(Animal):
    size = 85
    points = 70
    sprite = ASSETS_DIR / "dragon.png"